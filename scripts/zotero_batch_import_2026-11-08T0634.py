#!/usr/bin/env python3
"""Import dated BibLaTeX batches into Zotero through the connector endpoint.

Three subcommands, each deterministic and stateless (everything it reads comes
from the arguments, the batch files and the running Zotero; nothing is cached
between runs except the JSON it is told to save):

  check  OUTDIR BIB...   Read-only. Page through every library item, save the
                         pages under OUTDIR, and test every entry of every
                         batch three ways: equal DOI (decisive), citation key
                         already present in the item JSON or resolvable by
                         Better BibTeX (decisive), equal arXiv identifier
                         (decisive), equal or near-equal normalised title with
                         year within one (for judgement). Prints a table.
  import OUTDIR BIB [SKIPKEY...]
                         Write. POST the raw .bib text to /connector/import with
                         a session id derived from the batch filename (no
                         randomness), then /connector/updateSession to move the
                         session's items into self-ref-2026-cited. SKIPKEYs
                         (duplicates found by check) are cut from the text
                         sent. Refuses to run if any remaining key already
                         resolves, which also stops a second run.
  verify OUTDIR BIB [SKIPKEY...]
                         Read-only. For each entry: does the key resolve via
                         BBT (retried twice at 5 s), do title/DOI match, are
                         brace-protected words intact, and is the item in the
                         target collection.

MAINTAINER ONLY: this talks to a local Zotero API that exists only on the
maintainer's machine. It will not run for a contributor. Reads need no key;
the connector import needs none either, but it writes to the live library.
"""
import difflib, hashlib, json, os, re, sys, time, unicodedata, urllib.error, urllib.parse, urllib.request

HOST = 'http://127.0.0.1:23119'
API = HOST + '/api/users/0'
COLL_KEY = 'S8W5V4AL'             # self-ref-2026-cited (API key)
COLL_NAME = 'self-ref-2026-cited'
UA = 'zotero-batch-import/2026-11-08'


def req(method, url, body=None, ctype=None, extra=None, timeout=120):
    h = {'User-Agent': UA}
    if ctype:
        h['Content-Type'] = ctype
    if extra:
        h.update(extra)
    data = body.encode('utf-8') if isinstance(body, str) else body
    r = urllib.request.Request(url, data=data, method=method, headers=h)
    try:
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            return resp.status, dict(resp.headers), resp.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read().decode('utf-8', 'replace')


# ---------------------------------------------------------------- bib parsing
def parse_bib(path):
    """Minimal BibLaTeX reader: entry type, key, and top-level fields."""
    text = open(path, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'^@(\w+)\s*\{\s*([^,\s]+)\s*,', text, re.M):
        i, depth = m.end(), 1
        j = i
        while depth and j < len(text):
            c = text[j]
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
            j += 1
        body = text[i:j - 1]
        fields, k = {}, 0
        while k < len(body):
            fm = re.compile(r'\s*(\w+)\s*=\s*').match(body, k)
            if not fm:
                k += 1
                continue
            name, k = fm.group(1).lower(), fm.end()
            if k < len(body) and body[k] == '{':
                d, s = 1, k + 1
                k += 1
                while d and k < len(body):
                    if body[k] == '{':
                        d += 1
                    elif body[k] == '}':
                        d -= 1
                    k += 1
                fields[name] = body[s:k - 1]
            elif k < len(body) and body[k] == '"':
                e = body.index('"', k + 1)
                fields[name] = body[k + 1:e]
                k = e + 1
            else:
                e = re.compile(r'[^,]*').match(body, k).end()
                fields[name] = body[k:e].strip()
                k = e
        out.append({'type': m.group(1).lower(), 'key': m.group(2), 'fields': fields})
    return out


def norm_title(t):
    t = unicodedata.normalize('NFKD', t or '')
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'\\[a-zA-Z]+', ' ', t)
    return re.sub(r'[^a-z0-9]', '', t.lower())


def year_of(s):
    m = re.search(r'(1[5-9]\d\d|20\d\d)', s or '')
    return int(m.group(1)) if m else None


def norm_doi(d):
    d = (d or '').strip().lower()
    d = re.sub(r'^(https?://)?(dx\.)?doi\.org/', '', d)
    return d


def braced_words(title):
    return re.findall(r'\{([^{}]+)\}', title or '')


# ------------------------------------------------------------- library access
def all_items(outdir):
    items, start = [], 0
    os.makedirs(outdir, exist_ok=True)
    while True:
        st, _, body = req('GET', f'{API}/items?format=json&limit=100&start={start}')
        if st != 200:
            sys.exit(f'items page start={start}: HTTP {st}: {body[:300]}')
        with open(os.path.join(outdir, f'items_{start:05d}.json'), 'w', encoding='utf-8') as f:
            f.write(body)
        page = json.loads(body)
        if not page:
            break
        items.extend(page)
        start += 100
    return items


def bbt_resolves(key):
    q = urllib.parse.urlencode({'citationKeys': key, 'translator': 'biblatex'})
    st, _, body = req('GET', f'{HOST}/better-bibtex/export/item?{q}')
    return st == 200 and body.lstrip().startswith('@'), body


def collection_items(coll_key):
    keys, start = set(), 0
    while True:
        st, _, body = req('GET', f'{API}/collections/{coll_key}/items/top?format=json&limit=100&start={start}')
        page = json.loads(body) if st == 200 else []
        if not page:
            break
        for it in page:
            keys.add(it['data'].get('citationKey', ''))
        start += 100
    return keys


def coll_count(coll_key):
    st, _, body = req('GET', f'{API}/collections/{coll_key}')
    return json.loads(body)['meta']['numItems']


# ----------------------------------------------------------------- commands
def cmd_check(outdir, bibs):
    items = all_items(os.path.join(outdir, 'library_pages'))
    tops = [i['data'] for i in items if i['data'].get('itemType') not in ('note', 'attachment', 'annotation')]
    print(f'library: {len(items)} items paged, {len(tops)} regular items')
    by_doi, by_key, by_title, by_arxiv = {}, {}, {}, {}
    for d in tops:
        dois = {norm_doi(d.get('DOI'))}
        dois |= {norm_doi(x) for x in re.findall(r'(?im)^DOI:\s*(\S+)', d.get('extra') or '')}
        dois |= {norm_doi(x) for x in re.findall(r'doi\.org/(\S+)', d.get('url') or '')}
        for x in dois - {''}:
            by_doi.setdefault(x, []).append(d)
        blob = ' '.join([d.get('DOI') or '', d.get('extra') or '', d.get('url') or '', d.get('archiveID') or ''])
        for x in set(re.findall(r'(?i)arxiv[.:/ ]*(?:abs/)?(\d{4}\.\d{4,5})', blob)):
            by_arxiv.setdefault(x, []).append(d)
        ck = d.get('citationKey') or ''
        m = re.search(r'^Citation Key:\s*(\S+)', d.get('extra', ''), re.M)
        for k in {ck, m.group(1) if m else ''} - {''}:
            by_key.setdefault(k, []).append(d)
        by_title.setdefault(norm_title(d.get('title')), []).append(d)
    hits = 0
    for bib in bibs:
        ents = parse_bib(bib)
        print(f'\n== {os.path.basename(bib)}: {len(ents)} entries')
        for e in ents:
            f, k = e['fields'], e['key']
            doi = norm_doi(f.get('doi'))
            yr = year_of(f.get('date') or f.get('year'))
            found = []
            if k in by_key:
                found += [f"KEY in item {d['key']} ({d.get('citationKey')})" for d in by_key[k]]
            ok, _ = bbt_resolves(k)
            if ok and k not in by_key:
                found.append('KEY resolves via BBT')
            if doi and doi in by_doi:
                found += [f"DOI = item {d['key']} as {d.get('citationKey')}" for d in by_doi[doi]]
            ax = re.search(r'(\d{4}\.\d{4,5})', ' '.join([f.get('eprint') or '', f.get('url') or '', f.get('note') or '']))
            if ax:
                found += [f"ARXIV {ax.group(1)} = item {d['key']} as {d.get('citationKey')}"
                          for d in by_arxiv.get(ax.group(1), []) if not any(d['key'] in x for x in found)]
            nt = norm_title(f.get('title'))
            for d in by_title.get(nt, []) if nt else []:
                y2 = year_of(d.get('date'))
                if yr is None or y2 is None or abs(yr - y2) <= 1:
                    tag = f"TITLE~ item {d['key']} as {d.get('citationKey')} ({d.get('date')})"
                    if not any(d['key'] in x for x in found):
                        found.append(tag)
            # Looser title test, for judgement only: similarity >= 0.9 or one
            # normalised title a prefix of the other (subtitle dropped).
            if nt and len(nt) >= 12:
                for t2, ds in by_title.items():
                    if not t2 or t2 == nt or len(t2) < 12:
                        continue
                    if (t2.startswith(nt) or nt.startswith(t2) or
                            difflib.SequenceMatcher(None, nt, t2).quick_ratio() >= 0.9 and
                            difflib.SequenceMatcher(None, nt, t2).ratio() >= 0.9):
                        for d in ds:
                            y2 = year_of(d.get('date'))
                            if (yr is None or y2 is None or abs(yr - y2) <= 1) and \
                                    not any(d['key'] in x for x in found):
                                found.append(f"TITLE≈ item {d['key']} as {d.get('citationKey')} "
                                             f"({d.get('date')}): {d.get('title')[:70]!r}")
            if found:
                hits += 1
            print(f"  {k:45s} {'NEW' if not found else ' | '.join(found)}")
    print(f'\nentries with any match: {hits}')


def cmd_import(outdir, bib, skip=()):
    ents = [e for e in parse_bib(bib) if e['key'] not in skip]
    # Guard: refuse if any key already resolves (covers being run twice).
    present = [e['key'] for e in ents if bbt_resolves(e['key'])[0]]
    if present:
        sys.exit(f'REFUSED: keys already in library: {present}')
    os.makedirs(outdir, exist_ok=True)
    tag = os.path.splitext(os.path.basename(bib))[0]
    session = 'imp-' + hashlib.sha1(tag.encode()).hexdigest()[:16]
    before = coll_count(COLL_KEY)
    st, _, body = req('POST', HOST + '/connector/getSelectedCollection', '{}', 'application/json',
                      {'X-Zotero-Connector-API-Version': '3'})
    sel = json.loads(body)
    target = [t for t in sel.get('targets', []) if t['name'] == COLL_NAME]
    if len(target) != 1:
        sys.exit(f'target collection not found uniquely: {target}')
    target_id = target[0]['id']
    print(f'session {session}; selected in GUI: {sel.get("name")!r} id={sel.get("id")}; target {target_id}; '
          f'collection numItems before {before}')
    text = open(bib, encoding='utf-8').read()
    if skip:
        # Drop the skipped entries from the text sent; everything else verbatim.
        kept = []
        for chunk in re.split(r'(?m)^(?=@)', text):
            m = re.match(r'@\w+\s*\{\s*([^,\s]+)\s*,', chunk)
            if m and m.group(1) in skip:
                print(f'skipping {m.group(1)} (duplicate, left for the maintainer)')
                continue
            kept.append(chunk)
        text = ''.join(kept)
    st, hdr, body = req('POST', f'{HOST}/connector/import?session={session}', text, 'application/x-bibtex',
                        {'X-Zotero-Connector-API-Version': '3'})
    with open(os.path.join(outdir, f'import_{tag}.json'), 'w', encoding='utf-8') as f:
        f.write(body)
    print(f'import: HTTP {st}')
    created = []
    try:
        created = json.loads(body)
        print(f'import: {len(created)} items returned')
    except ValueError:
        print('import body:', body[:2000])
    if st != 201:
        sys.exit('import not 201; stopping')
    upd = json.dumps({'sessionID': session, 'target': target_id, 'tags': ''})
    st, _, body = req('POST', HOST + '/connector/updateSession', upd, 'application/json',
                      {'X-Zotero-Connector-API-Version': '3'})
    print(f'updateSession: HTTP {st} {body[:500]!r}')
    time.sleep(3)
    print(f'collection numItems after {coll_count(COLL_KEY)}')


def cmd_verify(outdir, bib, skip=()):
    ents = [e for e in parse_bib(bib) if e['key'] not in skip]
    os.makedirs(outdir, exist_ok=True)
    tag = os.path.splitext(os.path.basename(bib))[0]
    unresolved = [e['key'] for e in ents]
    exports = {}
    for attempt in range(3):
        for k in list(unresolved):
            ok, body = bbt_resolves(k)
            if ok:
                exports[k] = body
                unresolved.remove(k)
        if not unresolved:
            break
        if attempt < 2:
            time.sleep(5)
    with open(os.path.join(outdir, f'verify_{tag}.bib'), 'w', encoding='utf-8') as f:
        f.write(''.join(exports[e['key']] for e in ents if e['key'] in exports))
    in_coll = collection_items(COLL_KEY)
    bad = 0
    for e in ents:
        k, f = e['key'], e['fields']
        if k not in exports:
            print(f'  {k:45s} NOT RESOLVED')
            bad += 1
            continue
        ex = parse_bib_text(exports[k])
        exf = ex['fields'] if ex else {}
        exkey = ex['key'] if ex else '?'
        t_ok = norm_title(exf.get('title')) == norm_title(f.get('title'))
        d_ok = norm_doi(exf.get('doi')) == norm_doi(f.get('doi'))
        a_ok = norm_title(exf.get('author')) == norm_title(f.get('author'))
        lost = [w for w in braced_words(f.get('title')) if w not in (exf.get('title') or '')]
        coll = k in in_coll
        flag = 'OK' if (exkey == k and t_ok and d_ok and a_ok and not lost and coll) else 'CHECK'
        bad += flag != 'OK'
        print(f'  {k:45s} {flag} key={exkey == k} title={t_ok} author={a_ok} doi={d_ok} '
              f'braces_lost={lost} in_collection={coll}')
    print(f'{len(ents)} entries, {len(exports)} resolve, {bad} need attention')


def parse_bib_text(s):
    import tempfile
    with tempfile.NamedTemporaryFile('w', suffix='.bib', delete=False, encoding='utf-8') as t:
        t.write(s)
    try:
        r = parse_bib(t.name)
    finally:
        os.unlink(t.name)
    return r[0] if r else None


if __name__ == '__main__':
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    cmd, outdir, rest = sys.argv[1], sys.argv[2], sys.argv[3:]
    {'check': lambda: cmd_check(outdir, rest),
     'import': lambda: cmd_import(outdir, rest[0], tuple(rest[1:])),
     'verify': lambda: cmd_verify(outdir, rest[0], tuple(rest[1:]))}[cmd]()
