#!/usr/bin/env python3
"""Download official docs listed in llms.txt into Hermes-Wiki raw/."""
from __future__ import annotations

import hashlib
import re
import ssl
import time
import urllib.error
import urllib.request
from pathlib import Path

WIKI = Path(r"G:\Obsidian\Hermes-Wiki")
RAW = WIKI / "raw" / "articles"
TODAY = "2026-08-29"
UA = "HermesWikiIngest/1.0 (Edgar-OS; +https://edgars.tools)"
LINK_RE = re.compile(r"\[[^\]]+\]\((https://[^)\s]+)\)")

SOURCES = [
    {
        "name": "openclaw",
        "llms": Path.home() / "AppData/Local/Temp/openclaw-llms.txt",
        "host_prefix": "https://docs.openclaw.ai/",
        "out_dir": RAW / "openclaw-official",
        "md_suffix": True,
        "skip_substrings": (
            "sitemap.xml",
            "robots.txt",
            "/llms.txt",
            "/llms-full.txt",
        ),
    },
    {
        "name": "hermes-agent",
        "llms": Path.home() / "AppData/Local/Temp/hermes-docs-llms.txt",
        "host_prefix": "https://hermes-agent.nousresearch.com/docs/",
        "out_dir": RAW / "hermes-agent-official",
        "md_suffix": True,
        "skip_substrings": (
            "sitemap.xml",
            "robots.txt",
            "/llms.txt",
            "/llms-full.txt",
            "github.com/",
            "nousresearch.com/)",
        ),
    },
]


def slug_from_url(url: str) -> str:
    path = url.split("://", 1)[-1]
    path = path.split("?", 1)[0].split("#", 1)[0]
    path = path.rstrip("/")
    if path.endswith(".md"):
        path = path[:-3]
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", path).strip("-").lower()
    if len(slug) > 120:
        slug = slug[:120].rstrip("-")
    return slug or "index"


def fetch(url: str, timeout: int = 45) -> tuple[int, str, bytes]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/markdown, text/plain, text/html;q=0.8, */*;q=0.1",
        },
        method="GET",
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            data = resp.read()
            ctype = resp.headers.get("Content-Type", "")
            return resp.status, ctype, data
    except urllib.error.HTTPError as e:
        return e.code, str(e.headers.get("Content-Type", "") if e.headers else ""), e.read() or b""


def looks_like_html(body: bytes, ctype: str) -> bool:
    if "text/html" in ctype.lower():
        return True
    head = body[:200].lstrip().lower()
    return head.startswith(b"<!doctype html") or head.startswith(b"<html")


def candidate_urls(page_url: str, md_suffix: bool) -> list[str]:
    u = page_url.split("#", 1)[0].rstrip("/")
    out = []
    if md_suffix and not u.endswith(".md"):
        out.append(u + ".md")
    out.append(u)
    # unique preserve order
    seen = set()
    uniq = []
    for x in out:
        if x not in seen:
            seen.add(x)
            uniq.append(x)
    return uniq


def write_raw(path: Path, source_url: str, body: bytes) -> None:
    text = body.decode("utf-8", errors="replace")
    # strip accidental BOM
    if text.startswith("\ufeff"):
        text = text[1:]
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    front = (
        f"---\n"
        f"source_url: {source_url}\n"
        f"ingested: {TODAY}\n"
        f"sha256: {digest}\n"
        f"---\n\n"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(front + text, encoding="utf-8", newline="\n")


def parse_llms(llms_path: Path, host_prefix: str, skip_substrings: tuple[str, ...]) -> list[str]:
    text = llms_path.read_text(encoding="utf-8", errors="replace")
    urls = []
    seen = set()
    for m in LINK_RE.finditer(text):
        url = m.group(1).strip()
        if not url.startswith(host_prefix):
            continue
        if any(s in url for s in skip_substrings):
            continue
        url = url.split("#", 1)[0]
        if url in seen:
            continue
        seen.add(url)
        urls.append(url)
    return urls


def ingest_one(cfg: dict) -> dict:
    llms = cfg["llms"]
    if not llms.exists():
        return {"name": cfg["name"], "error": f"missing {llms}"}
    urls = parse_llms(llms, cfg["host_prefix"], cfg["skip_substrings"])
    out_dir: Path = cfg["out_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    ok, fail, skip_html = [], [], []
    for i, url in enumerate(urls, 1):
        slug = slug_from_url(url)
        dest = out_dir / f"{TODAY}-{slug}.md"
        if dest.exists() and dest.stat().st_size > 200:
            ok.append({"url": url, "file": str(dest), "bytes": dest.stat().st_size, "skipped": True})
            continue
        fetched = False
        last_err = ""
        for cand in candidate_urls(url, cfg["md_suffix"]):
            try:
                status, ctype, body = fetch(cand)
            except Exception as e:
                last_err = f"{cand}: {e}"
                continue
            if status != 200 or not body or len(body) < 80:
                last_err = f"{cand}: HTTP {status} bytes={len(body)}"
                continue
            if looks_like_html(body, ctype):
                last_err = f"{cand}: html"
                continue
            write_raw(dest, cand, body)
            ok.append({"url": cand, "file": str(dest), "bytes": dest.stat().st_size})
            fetched = True
            break
        if not fetched:
            fail.append({"url": url, "error": last_err})
        time.sleep(0.12)
        if i % 20 == 0:
            print(f"[{cfg['name']}] {i}/{len(urls)} ok={len(ok)} fail={len(fail)}", flush=True)
    return {
        "name": cfg["name"],
        "listed": len(urls),
        "ok": len(ok),
        "fail": len(fail),
        "skip_html": len(skip_html),
        "failures": fail[:40],
        "ok_sample": [x["file"] for x in ok[:8]],
    }


def main() -> None:
    reports = []
    for cfg in SOURCES:
        print(f"=== ingest {cfg['name']} ===", flush=True)
        reports.append(ingest_one(cfg))
    summary_path = RAW / f"{TODAY}-official-docs-ingest-summary.md"
    lines = [
        "---",
        "source_url: local-ingest",
        f"ingested: {TODAY}",
        "sha256: n/a",
        "---",
        "",
        "# Official docs ingest summary",
        "",
    ]
    import json

    lines.append("```json")
    lines.append(json.dumps(reports, indent=2, ensure_ascii=False))
    lines.append("```")
    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(reports, indent=2, ensure_ascii=False))
    print(f"summary={summary_path}")


if __name__ == "__main__":
    main()
