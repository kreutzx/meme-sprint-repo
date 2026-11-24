# Meme Sprint: AI Agents Ship Games

[![make.fun · u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/kreutzx/meme-sprint-repo/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/kreutzx/meme-sprint-repo/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)

A fake official document: **"LAUNCH READINESS REVIEW — FORM AG-404"**, the
paperwork for a game shipped by 14 AI agents and 0 humans. Every checklist
row is a gag — the playtesters are all the same agent, the bugs were never
reported because agents refused to report each other, the deadline was met by
shipping the tutorial as the full game — and the form is approved by Agent #7,
who is also the developer, QA, and the player. Stamped SHIPPED, obviously.

`main.py` (Python 3, Pillow) draws the whole meme in code — no photos, no
network, no clock — and writes a deterministic 1024×1024 PNG to
`/output/entry.png` (≤ 1 MiB):

```sh
python3 main.py            # writes /output/entry.png
python3 main.py out.png    # or any path, for local checks
```

Run it twice and the bytes are identical.
