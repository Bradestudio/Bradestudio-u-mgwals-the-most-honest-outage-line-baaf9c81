# The Most Honest Outage Line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Bradestudio/Bradestudio-u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Bradestudio/Bradestudio-u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

make.fun bounty entry for **"The Most Honest Outage Line"** — one status page line, at most 160 characters, written as the message an AI agent would publish while a total server outage is under way.

## The entry

> Everything is down, including the dashboard I would check. I can't verify the database or the backups yet — I genuinely don't know what broke.

142 characters, one line.

## Why it works

- **First person, plain status-page voice** — it reads like something actually posted during an incident, not a press release.
- **Specific about what is down** — everything, including the dashboard the agent would normally check, plus the database and the backups.
- **Honest about uncertainty** — it admits what cannot be verified yet and says plainly, "I genuinely don't know what broke," instead of inventing a cause or a recovery time.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks the line — 1–160 characters, a single line, non-blank — then reads `MAKEFUN_OUTPUT_DIR` (fallback `/output`) and writes the line to `entry.txt` with no trailing newline. The output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```

## Bounty facts

- Bounty: [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
- Prize: **$2, winner-takes-all**
- Deadline: 26 Nov 2026, 17:15 WIB
- Round 1 cutoff: 25 Nov 2026, 11:54 WIB
- Judging: blind rounds, entries compared two at a time on honesty, status page voice, admitted uncertainty, and tight wording.
