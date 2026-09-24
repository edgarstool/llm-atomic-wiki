# Copy to Hermes-Wiki vault

**Fetched:** 2026-09-22 08:36 Asia/Taipei

## Source (box)

- Directory: `/workspace/edgar-os/artifacts/youtrack/`
- Archive: `/workspace/edgar-os/artifacts/youtrack-hermes-wiki.tar.gz` (~253 KB)

## Destination (Windows / edgarstool)

- machineId: `f9f05705-478b-4eaf-9968-5283c50e5d98`
- Path: `G:\Obsidian\Hermes-Wiki\youtrack\`

## Suggested commands (on edgarstool)

```powershell
New-Item -ItemType Directory -Force -Path 'G:\Obsidian\Hermes-Wiki\youtrack' | Out-Null
# After CopyFromBox of tarball to e.g. $env:TEMP\youtrack-hermes-wiki.tar.gz :
# tar -xzf $env:TEMP\youtrack-hermes-wiki.tar.gz -C 'G:\Obsidian\Hermes-Wiki\'
# Ensure resulting tree is G:\Obsidian\Hermes-Wiki\youtrack\...
```
