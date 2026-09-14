#!/usr/bin/env python3
"""Classify every Zotero item carrying an `ISBN:` line in its Extra field.

Mendeley put an ISBN: line into Extra on import. Better BibTeX reads it as a
field injection and emits an `isbn` field, which is wrong on a journal article
and, where the value is not an ISBN at all, produces a biber warning.

Rule: a line is deleted only if its value fails ISBN-10/13 check-digit
validation. A valid ISBN is never deleted -- it is real metadata, and its
presence on a journalArticle means the item type is wrong, which is a
different fix. Other Extra lines (arXiv:, etc.) are preserved verbatim.


MAINTAINER ONLY: this talks to a local Zotero API and needs a key that
exists only on the maintainer's machine. It will not run for a contributor.
"""
import json, re, sys, urllib.request

SID = open('zotsid').read().strip()
BASE = 'http://127.0.0.1:23119/api/users/0'


def get(path):
    r = urllib.request.Request(BASE + path, headers={'Zotero-Server-ID': SID})
    return json.load(urllib.request.urlopen(r, timeout=60))


def valid_isbn(s):
    # Must LOOK like an ISBN before the check digit is even consulted: digits,
    # hyphens and spaces only, optional trailing X. This is what rejects arXiv
    # identifiers such as 1706.03762v7 and 9806054v229, several of which pass
    # the check digit by coincidence once punctuation is stripped.
    if not re.fullmatch(r'[0-9][0-9\- ]{7,}[0-9Xx]', s.strip()):
        return False
    t = re.sub(r'[^0-9Xx]', '', s)
    if len(t) == 10:
        tot = sum((10 - i) * (10 if c in 'Xx' else int(c)) for i, c in enumerate(t))
        return tot % 11 == 0
    if len(t) == 13:
        if not t.startswith(('978', '979')):   # the only assigned EAN prefixes
            return False
        tot = sum((1 if i % 2 == 0 else 3) * int(c) for i, c in enumerate(t))
        return tot % 10 == 0
    return False


def classify(v):
    if valid_isbn(v):
        return 'VALID-ISBN'
    if re.fullmatch(r'\d{4}\.\d{4,5}(v\d+)?', v) or re.search(r'v\d+$', v) \
       or re.fullmatch(r'[a-z-]+/\d{7}(v\d+)?', v):
        return 'arXiv-id'
    if re.fullmatch(r'\d{4}-?\d{3}[\dXx]', v):
        return 'ISSN-shaped'
    return 'unrecognised'


items, start = [], 0
while True:
    batch = get(f'/items?limit=100&start={start}&format=json')
    if not batch:
        break
    items += batch
    start += 100
print(f'scanned {len(items)} items', file=sys.stderr)

rows = []
for it in items:
    d = it['data']
    extra = d.get('extra', '') or ''
    if 'ISBN:' not in extra:
        continue
    keep, removed = [], []
    for line in extra.split('\n'):
        m = re.match(r'\s*ISBN\s*:\s*(.+?)\s*$', line, re.I)
        if m and classify(m.group(1)) != 'VALID-ISBN':
            removed.append((m.group(1), classify(m.group(1))))
        else:
            keep.append(line)
    rows.append({
        'key': d['key'], 'version': d['version'], 'type': d['itemType'],
        'citekey': d.get('citationKey'), 'title': (d.get('title') or '')[:58],
        'extra_before': extra, 'extra_after': '\n'.join(keep).strip(),
        'removed': removed,
        'kept_isbn': [l for l in keep if re.match(r'\s*ISBN\s*:', l, re.I)],
    })

json.dump(rows, open('isbn_sweep_plan.json', 'w'), indent=1)
print(f'{len(rows)} items carry an ISBN: line\n')
print(f"{'citekey':<44} {'type':<16} verdict")
print('-' * 92)
for r in sorted(rows, key=lambda r: (not r['removed'], r['citekey'] or '')):
    if r['removed']:
        for v, c in r['removed']:
            print(f"  {str(r['citekey']):<42} {r['type']:<16} DELETE  {c:<14} {v}")
    for l in r['kept_isbn']:
        print(f"  {str(r['citekey']):<42} {r['type']:<16} KEEP    valid ISBN     {l.split(':',1)[1].strip()}")
print()
print('to delete:', sum(len(r['removed']) for r in rows),
      '| to keep:', sum(len(r['kept_isbn']) for r in rows))
