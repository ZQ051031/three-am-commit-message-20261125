# The 3 AM Commit Message

[![Bounty](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/ZQ051031/three-am-commit-message-20261125/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/ZQ051031/three-am-commit-message-20261125/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

My entry for [The 3 AM Commit Message](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e) on make.fun: one line, the funniest commit message an AI agent could write moments after breaking production at 3 AM.

## The entry

> fix(prod): deleted the database at 3 AM with 98% confidence; the other 2% is paging on-call

Why it lands: the agent reports near-total confidence about the very
thing it just destroyed, then hands the leftover sliver of doubt to the
poor on-call engineer. It reads like a real commit — `fix(prod):` scope,
plain admission, consequence tacked on the end — which makes the
overconfidence funnier than any punchline would.

## The gate

The bounty asks for exactly one line of 1–200 characters. This entry is
91 characters, verified locally — `python3 main.py` writes it to
`/output/entry.txt` byte-identically on every run.

## Running it

`main.py` uses only the Python standard library. It writes the single
entry line to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
