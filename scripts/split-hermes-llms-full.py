#!/usr/bin/env python3
"""Split Hermes llms-full.txt into per-page raw articles + stamp frontmatter."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

WIKI = Path(r"G:\Obsidian\Hermes-Wiki")
RAW = WIKI / "raw" / "articles"
TODAY = "2026-08-29"
HERMES_FULL = RAW / f"{TODAY}-hermes-agent-llms-full.txt"
OPENCLAW_FULL = RAW / f"{TODAY}-openclaw-llms-full.txt"
OUT = RAW / "hermes-agent-official"
SRC_RE = re.compile(r"^<!-- source: ([^>]+) -->\s*$", re.M)


def sha256_text(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def stamp_frontmatter(path: Path, source_url: str) -> None:
    raw = path.read_text(encoding="utf-8", errors="replace")
    if raw.lstrip().startswith("---\n") and "source_url:" in raw[:400]:
        return
    body = raw
    digest = sha256_text(body)
    path.write_text(
        f"---\nsource_url: {source_url}\ningested: {TODAY}\nsha256: {digest}\n---\n\n{body}",
        encoding="utf-8",
        newline="\n",
    )


def split_hermes() -> dict:
    text = HERMES_FULL.read_text(encoding="utf-8", errors="replace")
    # drop existing frontmatter if we stamped it
    if text.startswith("---\n"):
        text = text.split("\n---\n", 1)[-1]
    matches = list(SRC_RE.finditer(text))
    OUT.mkdir(parents=True, exist_ok=True)
    written = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunk = text[start:end].strip() + "\n"
        src = m.group(1).strip()
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", src).strip("-").lower()
        if len(slug) > 120:
            slug = slug[:120].rstrip("-")
        dest = OUT / f"{TODAY}-{slug}.md"
        url = "https://hermes-agent.nousresearch.com/docs/" + src.replace(
            "website/docs/", ""
        ).replace(".md", "")
        body_only = chunk
        digest = sha256_text(body_only)
        dest.write_text(
            f"---\nsource_url: {url}\nsource_path: {src}\ningested: {TODAY}\nsha256: {digest}\n---\n\n{body_only}",
            encoding="utf-8",
            newline="\n",
        )
        written.append(str(dest.name))
    return {"pages": len(written), "dir": str(OUT), "sample": written[:8]}


def main() -> None:
    stamp_frontmatter(HERMES_FULL, "https://hermes-agent.nousresearch.com/docs/llms-full.txt")
    if OPENCLAW_FULL.exists():
        stamp_frontmatter(OPENCLAW_FULL, "https://docs.openclaw.ai/llms-full.txt")
    report = split_hermes()
    oc = list((RAW / "openclaw-official").glob("*.md")) if (RAW / "openclaw-official").exists() else []
    report["openclaw_pages"] = len(oc)
    report["hermes_full_bytes"] = HERMES_FULL.stat().st_size
    report["openclaw_full_bytes"] = OPENCLAW_FULL.stat().st_size if OPENCLAW_FULL.exists() else 0
    import json

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
