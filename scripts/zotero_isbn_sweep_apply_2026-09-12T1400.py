#!/usr/bin/env python3
"""Apply the ISBN sweep: remove Extra lines that are not ISBNs.

Reads isbn_sweep_plan.json (which holds each item's Extra field before the
edit, so the sweep is reversible), and PATCHes only items with something to
remove. Each PATCH is guarded by If-Unmodified-Since-Version, so an item
changed since the scan is skipped rather than clobbered.


MAINTAINER ONLY: this talks to a local Zotero API and needs a key that
exists only on the maintainer's machine. It will not run for a contributor.
"""
import json, urllib.request, urllib.error

SID = open('zotsid').read().strip()
KEY = open('zotkey').read().strip()
BASE = 'http://127.0.0.1:23119/api/users/0'

rows = json.load(open('isbn_sweep_plan.json'))
todo = [r for r in rows if r['removed']]
print(f'{len(todo)} items to patch\n')

ok = skipped = failed = 0
for r in todo:
    body = json.dumps({'extra': r['extra_after']}).encode()
    req = urllib.request.Request(
        f"{BASE}/items/{r['key']}", data=body, method='PATCH',
        headers={'Zotero-Server-ID': SID, 'Zotero-API-Key': KEY,
                 'Content-Type': 'application/json',
                 'If-Unmodified-Since-Version': str(r['version'])})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            code = resp.status
        removed = ', '.join(f'{v} [{c}]' for v, c in r['removed'])
        print(f"  {code}  {str(r['citekey']):<46} removed {removed}")
        ok += 1
    except urllib.error.HTTPError as e:
        if e.code == 412:
            print(f"  412 SKIPPED (changed since scan) {r['citekey']}")
            skipped += 1
        else:
            print(f"  {e.code} FAILED {r['citekey']}: {e.read()[:100]}")
            failed += 1

print(f'\npatched {ok}, skipped {skipped}, failed {failed}')
