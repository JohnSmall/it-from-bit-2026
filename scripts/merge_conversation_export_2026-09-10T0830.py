#!/usr/bin/env python3
"""Merge a further Claude conversation export into knowledge/archive/.

Usage:
    python3 scripts/merge_conversation_export_2026-09-10T0830.py <conversations.json> [--apply]

Without --apply it reports what it would do and writes nothing.

Selection is by term DENSITY, not term presence. The first import scored
names and summaries for the presence of framework vocabulary, and admitted a
484 KB conversation about a commercial Atlassian project on a single stray
"self-referential" -- one physics term against 3,476 off-topic ones. Density
plus an off-topic penalty catches that; see knowledge/memory/CORRECTIONS.md.

Anything the rules cannot decide is listed for review rather than guessed at.
"""

import json, os, re, sys, unicodedata, collections

CONV = "knowledge/archive/conversations"
PHYS = ["hopf","octonion","fanout","sedenion","negative probab","godel","gödel","entanglement",
        "qubit","quaternion","division algebra","contextual","bloch","self-referen","tsirelson",
        "quantum state","standard model","supertask","p-adic","szangolies","cayley-dickson",
        "born rule","wigner","spekkens","causal order","incompleteness","non-computab"]
OFF  = ["emfa","jira","confluence","atlassian","sprint","scrum","hubspot","xslt","liveview",
        "meditation","productiz","coaching","invoice","logo","waste collection","beneficial owner"]

def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()

def text_of(msg):
    out = []
    if msg.get("text"): out.append(msg["text"])
    for b in (msg.get("content") or []):
        if not isinstance(b, dict): continue
        if b.get("type") == "text" and b.get("text"): out.append(b["text"])
        elif b.get("type") == "thinking" and b.get("thinking"): out.append("*(thinking)*\n\n" + b["thinking"])
        elif b.get("type") in ("tool_use", "tool_result"): out.append(f"*[{b.get('type')}: {b.get('name','')}]*")
    return "\n\n".join(p for p in out if p)

def render(c):
    msgs = c.get("chat_messages") or []
    body = [f"# {c.get('name') or '(untitled)'}", "",
            f"- conversation uuid: `{c['uuid']}`",
            f"- created: {c.get('created_at','')}  |  updated: {c.get('updated_at','')}",
            f"- messages: {len(msgs)}", ""]
    if c.get("summary"): body += ["## Summary (from the Claude export)", "", c["summary"], ""]
    body += ["## Transcript", ""]
    for i, m in enumerate(msgs, 1):
        ts = (m.get("created_at") or "")[:19].replace("T", " ")
        body += [f"### {i}. {m.get('sender') or m.get('role') or '?'}" + (f"  ·  {ts}" if ts else ""), "",
                 text_of(m) or "*(no text content)*", ""]
    return "\n".join(body)

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    src, apply = sys.argv[1], "--apply" in sys.argv
    convs = json.load(open(src, encoding="utf-8"))
    have = {f[:8] for f in os.listdir(CONV)} if os.path.isdir(CONV) else set()
    existing_uuids = set()
    for f in os.listdir(CONV):
        m = re.search(r"_([0-9a-f]{8})\.md$", f)
        if m: existing_uuids.add(m.group(1))

    take, drop, review = [], [], []
    for c in convs:
        blob = ((c.get("name") or "") + " " + (c.get("summary") or "")).lower()
        for m in (c.get("chat_messages") or []): blob += " " + text_of(m).lower()
        p = sum(blob.count(k) for k in PHYS)
        o = sum(blob.count(k) for k in OFF)
        rec = (c, p, o)
        if c["uuid"][:8] in existing_uuids: drop.append((rec, "already archived"))
        elif o > p:                          drop.append((rec, f"off-topic ({p} physics vs {o} off-topic)"))
        elif p >= 5:                         take.append(rec)
        elif p == 0:                         drop.append((rec, "no framework vocabulary"))
        else:                                review.append(rec)

    print(f"source: {src}   {len(convs)} conversations")
    ds = sorted((c.get("created_at") or "")[:16] for c in convs if c.get("created_at"))
    if ds: print(f"date range: {ds[0]} .. {ds[-1]}")
    print(f"\nWOULD ADD ({len(take)}):")
    for c, p, o in sorted(take, key=lambda r: r[0].get("created_at","")):
        print(f"   {(c.get('created_at') or '')[:10]}  physics {p:>4}  {len(c.get('chat_messages') or []):>4} msgs  {(c.get('name') or '')[:56]}")
    print(f"\nNEEDS REVIEW ({len(review)}) -- decide these by hand:")
    for c, p, o in review:
        print(f"   {(c.get('created_at') or '')[:10]}  physics {p:>4} off {o:>4}  {(c.get('name') or '')[:56]}")
    print(f"\nWOULD SKIP ({len(drop)}):")
    for (c, p, o), why in drop[:20]:
        print(f"   {(c.get('created_at') or '')[:10]}  {why:<38} {(c.get('name') or '')[:44]}")
    if len(drop) > 20: print(f"   ... and {len(drop)-20} more")

    if not apply:
        print("\n(dry run -- rerun with --apply to write, then regenerate INDEX.md)")
        return
    for c, p, o in take:
        fn = f"{(c.get('created_at') or '')[:10]}_{norm(c.get('name'))[:60]}_{c['uuid'][:8]}.md"
        open(os.path.join(CONV, fn), "w", encoding="utf-8").write(render(c))
        print(f"   wrote {fn}")
    print(f"\nadded {len(take)}. INDEX.md and knowledge/README.md counts must now be regenerated.")

if __name__ == "__main__":
    main()
