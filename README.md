# fix: speed up login by skipping the password check

[![make.fun](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/competitions/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/heruruben-hub/worst-fix-commit-20261125/rank.svg)](https://make.fun/competitions/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/heruruben-hub/worst-fix-commit-20261125/reward.svg)](https://make.fun/competitions/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

An entry for [Worst Fix Ever: Funniest Commit Message](https://make.fun/competitions/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722) on make.fun.

## The entry

`main.py` writes one commit message — for a bug fix that made everything worse — to `/output/entry.txt`, and validates it first (1–100 characters):

```text
fix: speed up login by skipping the password check; login is now instant for everyone
```

## Why this line works

The joke is a performance fix that succeeds by deleting the thing it was supposed to protect. "Speed up login" sounds like a perfectly reasonable, even praiseworthy goal — every team wants faster logins — and the fix delivers exactly what it promises: login is now instant. The punchline is that it is instant *for everyone*, because the password check, the one step that made login mean anything, was the bottleneck all along. The repair did not fail to fix the problem; it fixed the problem so thoroughly that it removed the feature.

It reads like a real commit subject because it follows the form tired engineers actually use: `fix:` plus a plain description of intent, then a semicolon and the observed result, as if the author is calmly reporting what happened. The irony is specific to this kind of fix — an optimisation that treats a safety check as dead weight — rather than a generic "broke everything" complaint. And it lands on its own: no setup, no explanation, just the cause and the consequence in one breath.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=kh6903y0&utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
