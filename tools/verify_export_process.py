#!/usr/bin/env python3
"""Export a verification agent's transcript (Claude Code subagent JSONL) into
data/verification/process/ as (1) the raw JSONL and (2) a readable Markdown log
of every tool call, every tool result (web fetches, greps, file reads) and every
piece of reasoning text — so the whole verification process can be audited.

    python3 tools/verify_export_process.py <transcript.jsonl> <label>
"""
import sys, os, json, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "verification", "process")


def blocks(msg):
    c = msg.get("content")
    if isinstance(c, str):
        return [{"type": "text", "text": c}]
    return c or []


def main(src, label):
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(src, os.path.join(OUT, f"{label}.jsonl"))
    lines = [f"# Verification process log — {label}\n"]
    n_calls = 0
    for line in open(src, encoding="utf-8"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        t = d.get("type")
        if t not in ("user", "assistant"):
            continue
        ts = d.get("timestamp", "")
        for b in blocks(d.get("message", {})):
            bt = b.get("type")
            if bt == "text" and b.get("text", "").strip():
                who = "AGENT" if t == "assistant" else "INPUT"
                lines.append(f"\n## [{ts}] {who}\n\n{b['text'].strip()}\n")
            elif bt == "thinking" and b.get("thinking", "").strip():
                lines.append(f"\n## [{ts}] AGENT (thinking)\n\n{b['thinking'].strip()}\n")
            elif bt == "tool_use":
                n_calls += 1
                inp = b.get("input", {})
                lines.append(f"\n## [{ts}] TOOL CALL #{n_calls}: {b.get('name')}\n\n```json\n{json.dumps(inp, ensure_ascii=False, indent=1)}\n```\n")
            elif bt == "tool_result":
                content = b.get("content")
                if isinstance(content, list):
                    content = "\n".join(x.get("text", "") for x in content if isinstance(x, dict))
                content = str(content or "")
                lines.append(f"\n### [{ts}] TOOL RESULT\n\n```\n{content}\n```\n")
    md = os.path.join(OUT, f"{label}.md")
    open(md, "w", encoding="utf-8").write("\n".join(lines))
    print(md, n_calls, "tool calls")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
