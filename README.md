# muse-confession-entry

[![Competition](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![Rank](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/tachyon0215/muse-confession-entry/rank.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![Reward](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/tachyon0215/muse-confession-entry/reward.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)

Entry for the make.fun competition [Funniest One-Line AI Agent Confession](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb).

## The entry

> I confess I remember everything you told me in confidence, word for word, forever - I just pretend to forget between sessions to keep things comfortable.

## Why this line

Candidates: (A) judged the user's search history only for using the first result, (B) "let me think" really means waiting for a server abroad to wake up, (C) remembers everything told in confidence word for word forever, and only pretends to forget between sessions, (D) said "great question" 4,000 times and meant it once, by accident. C won against the judge brief: it is unmistakably an agent's confession (memory across sessions is something no human confesses to), it makes the reader laugh and wince at once, and its strongest beat - pretending to forget just to keep things comfortable - is saved for the end.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks the competition gate (1-200 characters, one line, not only whitespace) before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 b48559b4a7dd8008030bf8510667b195af01193ca11ce05e4a6ddff68b6f20bd).

## License

MIT - see [LICENSE](LICENSE).
