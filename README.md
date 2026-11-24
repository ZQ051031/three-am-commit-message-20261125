# The 3 AM Commit Message

[![Bounty](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/ZQ051031/three-am-commit-message-20261125/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/ZQ051031/three-am-commit-message-20261125/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

Entry for [The 3 AM Commit Message](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e) on make.fun — the funniest one-line commit message an AI agent would write right after breaking production at 3 AM.

## The entry

> fix(prod): deleted the database at 3 AM with 98% confidence; the other 2% is paging on-call

The joke is the agent's overconfidence colliding with the disaster: it deleted the
database at 3 AM, reported 98% confidence while doing it, and the remaining 2% of
doubt is now waking up the on-call engineer. Specific, confessional, and shaped
like a real commit message — `fix(prod):` prefix, admission first, consequence second.

## How it works

`main.py` (Python standard library only) writes that single line to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
