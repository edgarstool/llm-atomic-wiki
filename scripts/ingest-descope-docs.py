#!/usr/bin/env python3
"""Ingest Descope docs: download llms index + full corpus, split, denoise, dedupe."""
from __future__ import annotations

import hashlib
import json
import re
import ssl
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

WIKI = Path(r"G:\Obsidian\Hermes-Wiki")
RAW = WIKI / "raw" / "articles"
OUT = RAW / "descope-official"
TODAY = "2026-09-21"
BASE = "https://docs.descope.com"
UA = "HermesWikiIngest/1.0 (Edgar-OS; +https://edgars.tools)"

PAGE_HDR_RE = re.compile(r"^# (.+?) \((/[^)]*)\)\s*$", re.M)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+)\)")
AGENT_BANNER_RE = re.compile(
    r"^> For AI agents:.*(?:\n>.*)*\n+(?:---\n+)?",
    re.M,
)
MULTI_BLANK_RE = re.compile(r"\n{3,}")
ZW_RE = re.compile(r"[\u200b\u200c\u200d\ufeff]")
# Mintlify / docs chrome leftovers occasionally leaked into exports
NOISE_LINE_RE = re.compile(
    r"^(?:"
    r"Was this (?:page|article) helpful\??|"
    r"On this page|"
    r"Copy page|"
    r"Ask AI|"
    r"Powered by Mintlify|"
    r"©\s*\d{4}\s*Descope|"
    r"Edit on GitHub|"
    r"Last updated on .+"
    r")\s*$",
    re.I,
)

FRAMEWORKS = (
    "react-native",
    "tanstack-router",
    "sveltekit",
    "nextauth",
    "next.js",
    "nextjs",
    "vue.js",
    "vuejs",
    "angular",
    "flutter",
    "kotlin",
    "swift",
    "react",
    "html",
    "dotnet",
    ".net",
)
BACKENDS = ("python", "go", "nodejs", "java", "ruby", "django", "php")
FW_ALT = "|".join(re.escape(f) for f in sorted(FRAMEWORKS, key=len, reverse=True))
BE_ALT = "|".join(BACKENDS)
GS_BACKEND_RE = re.compile(
    rf"^/getting-started/(?:{FW_ALT})/({BE_ALT})$",
    re.I,
)
FW_TOKEN_RE = re.compile(rf"\b(?:{FW_ALT})\b", re.I)


def fetch(url: str, timeout: int = 120) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/markdown, text/plain, */*;q=0.1",
        },
        method="GET",
    )
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return resp.read()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def slug_from_path(path: str) -> str:
    slug = path.strip("/").replace("/", "-") or "index"
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", slug).strip("-").lower()
    if len(slug) > 140:
        slug = slug[:140].rstrip("-")
    return slug


def denoise(text: str) -> str:
    text = ZW_RE.sub("", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if text.startswith("\ufeff"):
        text = text[1:]
    text = AGENT_BANNER_RE.sub("", text)
    lines = []
    for line in text.split("\n"):
        if NOISE_LINE_RE.match(line.strip()):
            continue
        lines.append(line)
    text = "\n".join(lines)
    text = MULTI_BLANK_RE.sub("\n\n", text).strip() + "\n"
    return text


def normalize_for_dedupe(path: str, body: str) -> str:
    """Collapse framework-name-only variants for getting-started backends."""
    text = body
    m = GS_BACKEND_RE.match(path)
    if m:
        be = m.group(1).lower()
        text = FW_TOKEN_RE.sub("FRAMEWORK", text)
        text = re.sub(
            rf"/getting-started/(?:{FW_ALT})/{be}",
            f"/getting-started/FRAMEWORK/{be}",
            text,
            flags=re.I,
        )
        text = re.sub(r"# .+? \(/getting-started/FRAMEWORK/", "# X (/getting-started/FRAMEWORK/", text)
    # ignore image alt/path churn and absolute vs relative asset hosts
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "![img]()", text)
    text = re.sub(r"https?://docs\.descope\.com", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = MULTI_BLANK_RE.sub("\n\n", text)
    return text.strip().lower()


def parse_llms_index(text: str) -> list[str]:
    paths: list[str] = []
    seen: set[str] = set()
    for m in LINK_RE.finditer(text):
        href = m.group(1).strip()
        if href.startswith("http://") or href.startswith("https://"):
            if not href.startswith(BASE):
                continue
            path = href[len(BASE) :] or "/"
        elif href.startswith("/"):
            path = href
        else:
            continue
        path = path.split("#", 1)[0].split("?", 1)[0] or "/"
        if path in seen:
            continue
        if any(s in path for s in ("/llms.txt", "/llms-full.txt", "sitemap.xml", "robots.txt")):
            continue
        seen.add(path)
        paths.append(path)
    return paths


def split_full(text: str) -> list[tuple[str, str, str]]:
    """Return list of (path, title, body)."""
    # drop stamped frontmatter if present
    if text.startswith("---\n"):
        parts = text.split("\n---\n", 1)
        if len(parts) == 2:
            text = parts[1]
    matches = list(PAGE_HDR_RE.finditer(text))
    pages: list[tuple[str, str, str]] = []
    for i, m in enumerate(matches):
        title, path = m.group(1).strip(), m.group(2).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = denoise(text[start:end])
        pages.append((path, title, body))
    return pages


def write_page(path: str, title: str, body: str, extra: dict | None = None) -> Path:
    dest = OUT / f"{TODAY}-{slug_from_path(path)}.md"
    digest = sha256_text(body)
    meta = {
        "source_url": f"{BASE}{path}" if path != "/" else f"{BASE}/",
        "path": path,
        "title": title,
        "ingested": TODAY,
        "sha256": digest,
    }
    if extra:
        meta.update(extra)
    # YAML-ish frontmatter (quote titles with colon)
    def yv(v: object) -> str:
        if isinstance(v, bool):
            return "true" if v else "false"
        s = str(v)
        if any(c in s for c in (":", "#", "{", "}", "[", "]", ",", '"', "'")):
            return json.dumps(s, ensure_ascii=False)
        return s

    fm = "---\n" + "\n".join(f"{k}: {yv(v)}" for k, v in meta.items()) + "\n---\n\n"
    dest.write_text(fm + body, encoding="utf-8", newline="\n")
    return dest


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)

    llms_path = RAW / f"{TODAY}-descope-llms.txt"
    full_path = RAW / f"{TODAY}-descope-llms-full.txt"

    print("Downloading llms.txt ...", flush=True)
    llms_bytes = fetch(f"{BASE}/llms.txt")
    llms_path.write_bytes(llms_bytes)
    print(f"  -> {llms_path} ({len(llms_bytes)} bytes)", flush=True)

    print("Downloading llms-full.txt ...", flush=True)
    full_bytes = fetch(f"{BASE}/llms-full.txt")
    full_path.write_bytes(full_bytes)
    print(f"  -> {full_path} ({len(full_bytes)} bytes)", flush=True)

    # stamp full dump
    full_text = full_bytes.decode("utf-8", errors="replace")
    stamped = (
        f"---\nsource_url: {BASE}/llms-full.txt\ningested: {TODAY}\n"
        f"sha256: {sha256_text(full_text)}\nbytes: {len(full_bytes)}\n---\n\n{full_text}"
    )
    full_path.write_text(stamped, encoding="utf-8", newline="\n")

    index_paths = parse_llms_index(llms_bytes.decode("utf-8", errors="replace"))
    pages = split_full(full_text)
    by_path = {p: (t, b) for p, t, b in pages}

    # fill gaps from index via .md fetch (small set expected)
    missing = [p for p in index_paths if p not in by_path]
    fetched_gap = []
    for i, path in enumerate(missing, 1):
        url = f"{BASE}{path}.md" if path != "/" else f"{BASE}/index.md"
        try:
            raw = fetch(url, timeout=45).decode("utf-8", errors="replace")
        except Exception as e:
            print(f"  gap fail {path}: {e}", flush=True)
            continue
        if len(raw) < 40 or raw.lstrip().lower().startswith("<!doctype"):
            continue
        body = denoise(raw)
        # ensure header has path
        title = path.strip("/") or "Overview"
        m = PAGE_HDR_RE.search(body)
        if m:
            title, path = m.group(1).strip(), m.group(2).strip()
        else:
            body = f"# {title} ({path})\n\n{body}"
        by_path[path] = (title, body)
        fetched_gap.append(path)
        time.sleep(0.08)
        if i % 25 == 0:
            print(f"  gap fetch {i}/{len(missing)}", flush=True)

    # exact + near dedupe
    exact_groups: dict[str, list[str]] = defaultdict(list)
    near_groups: dict[str, list[str]] = defaultdict(list)
    for path, (title, body) in by_path.items():
        exact_groups[sha256_text(body)].append(path)
        near_groups[sha256_text(normalize_for_dedupe(path, body))].append(path)

    drop_exact: set[str] = set()
    for paths in exact_groups.values():
        if len(paths) < 2:
            continue
        keep = sorted(paths, key=lambda p: (len(p), p))[0]
        for p in paths:
            if p != keep:
                drop_exact.add(p)

    drop_near: set[str] = set()
    near_map: dict[str, str] = {}  # dropped -> canonical
    for paths in near_groups.values():
        if len(paths) < 2:
            continue
        # prefer top-level /getting-started/{backend}, else common frontends
        fw_pref = {
            "nextjs": 0,
            "react": 1,
            "vue.js": 2,
            "sveltekit": 3,
            "angular": 4,
            "html": 5,
            "flutter": 6,
            "react-native": 7,
            "kotlin": 8,
            "swift": 9,
            "tanstack-router": 10,
        }

        def rank(p: str) -> tuple:
            if not GS_BACKEND_RE.match(p):
                return (0, 0, len(p), p)
            parts = p.strip("/").split("/")
            fw = parts[1].lower() if len(parts) >= 3 else ""
            return (1, fw_pref.get(fw, 50), len(p), p)

        keep = sorted(paths, key=rank)[0]
        for p in paths:
            if p == keep or p in drop_exact:
                continue
            # only auto-drop near-dupes for getting-started backend variants
            if GS_BACKEND_RE.match(p) and (GS_BACKEND_RE.match(keep) or keep.startswith("/getting-started/")):
                drop_near.add(p)
                near_map[p] = keep
            elif GS_BACKEND_RE.match(p) and any(GS_BACKEND_RE.match(x) for x in paths):
                drop_near.add(p)
                near_map[p] = keep

    kept = []
    stubs = []
    for path in sorted(by_path.keys()):
        title, body = by_path[path]
        if path in drop_exact:
            continue
        if path in drop_near:
            canon = near_map[path]
            stub = (
                f"# {title} ({path})\n\n"
                f"> Deduped: content is a framework-variant of `{canon}`.\n\n"
                f"Canonical: [{canon}]({BASE}{canon}.md)\n"
            )
            write_page(
                path,
                title,
                stub,
                {
                    "deduped": True,
                    "canonical_path": canon,
                    "kind": "stub",
                },
            )
            stubs.append({"path": path, "canonical": canon})
            continue
        write_page(path, title, body, {"kind": "page"})
        kept.append(path)

    # clean merged corpus (kept pages only, no stubs)
    merged_parts = []
    for path in kept:
        title, body = by_path[path]
        merged_parts.append(body.rstrip() + "\n")
    merged = "\n\n".join(merged_parts) + "\n"
    merged_path = RAW / f"{TODAY}-descope-docs-clean.md"
    merged_path.write_text(
        f"---\nsource_url: {BASE}/llms-full.txt\ningested: {TODAY}\n"
        f"pages: {len(kept)}\nsha256: {sha256_text(merged)}\n---\n\n{merged}",
        encoding="utf-8",
        newline="\n",
    )

    report = {
        "source": BASE,
        "ingested": TODAY,
        "llms_index_paths": len(index_paths),
        "full_split_pages": len(pages),
        "gap_fetched": len(fetched_gap),
        "gap_paths_sample": fetched_gap[:20],
        "total_unique_paths": len(by_path),
        "kept_pages": len(kept),
        "exact_dup_dropped": len(drop_exact),
        "near_dup_stubs": len(stubs),
        "exact_dup_groups": sum(1 for v in exact_groups.values() if len(v) > 1),
        "near_dup_groups": sum(1 for v in near_groups.values() if len(v) > 1),
        "out_dir": str(OUT),
        "clean_merged": str(merged_path),
        "clean_merged_bytes": merged_path.stat().st_size,
        "full_bytes": len(full_bytes),
        "stub_sample": stubs[:15],
        "missing_after": [p for p in index_paths if p not in by_path][:30],
    }
    report_path = RAW / f"{TODAY}-descope-ingest-report.md"
    report_path.write_text(
        "---\nsource_url: local-ingest\ningested: "
        + TODAY
        + "\nsha256: n/a\n---\n\n# Descope docs ingest report\n\n```json\n"
        + json.dumps(report, indent=2, ensure_ascii=False)
        + "\n```\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"report={report_path}")


if __name__ == "__main__":
    main()
