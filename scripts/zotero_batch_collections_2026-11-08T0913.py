#!/usr/bin/env python3
"""Move the 85 items imported on 2026-11-08 out of self-ref-2026-cited into
one top-level collection per batch, named after the batch's .bib stem.

Only kimura2003bloch is cited in Paper 1, so it alone stays in
self-ref-2026-cited (the collection Better BibTeX exports to
paper1/references.bib) and is also filed in its batch collection. The other
84 leave the exported collection but stay in the library.

Usage:
  zotero_batch_collections_2026-11-08T0913.py IMPORT_DIR SIDFILE KEYFILE [--only BATCH]

IMPORT_DIR holds import_<stem>.json, the item lists /connector/import returned
(written by zotero_batch_import_2026-11-08T0634.py). SIDFILE and KEYFILE hold
the Zotero-Server-ID and the local API key; the key is read from the file and
never printed. Deterministic and idempotent: a collection is created only if
no top-level collection of that name exists, and an item already carrying
exactly the wanted collections is left alone. Each PATCH carries
If-Unmodified-Since-Version from a fresh GET; a 412 is reported and skipped,
never forced.

MAINTAINER ONLY: this talks to a local Zotero API and needs a key that
exists only on the maintainer's machine. It will not run for a contributor.
"""
import json, os, sys, urllib.error, urllib.request

API = 'http://127.0.0.1:23119/api/users/0'
CITED_COLL = 'S8W5V4AL'                     # self-ref-2026-cited
KEEP = {'kimura2003bloch'}                  # cited in Paper 1
BATCHES = ['qutrit_hopf_refs_2026-11-07T1610', 'b_anomaly_refs_2026-11-07T1910',
           'three_papers_lfu_refs_2026-11-07T2010', 'confinement_flux_tube_refs_2026-11-07T1140',
           'lattice_causal_set_refs_2026-11-07T0710']


def call(method, path, sid, key=None, body=None, extra=None):
    h = {'Zotero-Server-ID': sid, 'User-Agent': 'zotero-batch-collections/2026-11-08'}
    if key:
        h['Zotero-API-Key'] = key
    if body is not None:
        h['Content-Type'] = 'application/json'
        body = json.dumps(body).encode()
    if extra:
        h.update(extra)
    r = urllib.request.Request(API + path, data=body, method=method, headers=h)
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def collections(sid):
    out, start = [], 0
    while True:
        st, b = call('GET', f'/collections?format=json&limit=100&start={start}', sid)
        page = json.loads(b)
        if not page:
            return out
        out += page
        start += 100


def main():
    imp, sidf, keyf = sys.argv[1:4]
    only = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else None
    sid, key = open(sidf).read().strip(), open(keyf).read().strip()
    batches = [b for b in BATCHES if only in (None, b)]
    # 1. collections, created only if absent
    existing = {}
    for c in collections(sid):
        if c['data'].get('parentCollection') in (False, None):
            existing.setdefault(c['data']['name'], []).append(c['key'])
    ckey = {}
    for b in batches:
        if b in existing:
            if len(existing[b]) != 1:
                sys.exit(f'{b}: {len(existing[b])} collections of that name; refusing')
            ckey[b] = existing[b][0]
            print(f'collection {b}: exists, key {ckey[b]}')
            continue
        st, body = call('POST', '/collections', sid, key, [{'name': b, 'parentCollection': False}])
        res = json.loads(body) if body.strip().startswith('{') else {}
        succ = res.get('successful') or res.get('success') or {}
        if st != 200 or '0' not in succ:
            sys.exit(f'create {b}: HTTP {st}: {body[:500]}')
        v = succ['0']
        ckey[b] = v if isinstance(v, str) else v['key']
        print(f'collection {b}: created, key {ckey[b]}')
    # 2. items
    for b in batches:
        items = [i for i in json.load(open(os.path.join(imp, f'import_{b}.json'))) if i.get('citationKey')]
        counts = {'moved': 0, 'unchanged': 0, 'skipped_412': 0, 'failed': 0}
        for it in sorted(items, key=lambda i: i['citationKey']):
            st, body = call('GET', f"/items/{it['key']}?format=json", sid)
            if st != 200:
                print(f"  {it['citationKey']}: GET HTTP {st}"); counts['failed'] += 1; continue
            d = json.loads(body)['data']
            if d.get('citationKey') != it['citationKey']:
                print(f"  {it['citationKey']}: item {it['key']} now has key {d.get('citationKey')}; skipped")
                counts['failed'] += 1; continue
            want = [CITED_COLL, ckey[b]] if it['citationKey'] in KEEP else [ckey[b]]
            if sorted(d.get('collections', [])) == sorted(want):
                counts['unchanged'] += 1; continue
            st, body = call('PATCH', f"/items/{it['key']}", sid, key, {'collections': want},
                            {'If-Unmodified-Since-Version': str(d['version'])})
            if st == 204:
                counts['moved'] += 1
                print(f"  {it['citationKey']:45s} {it['key']} v{d['version']} {d.get('collections')} -> {want}")
            elif st == 412:
                counts['skipped_412'] += 1
                print(f"  {it['citationKey']}: 412, changed under us; skipped")
            else:
                counts['failed'] += 1
                print(f"  {it['citationKey']}: PATCH HTTP {st}: {body[:300]}")
        print(f'{b}: {len(items)} items, {counts}')


if __name__ == '__main__':
    main()
