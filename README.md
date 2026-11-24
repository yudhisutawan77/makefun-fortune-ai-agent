# Fortune Cookie for an AI Agent

![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)
![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/yudhisutawan77/makefun-fortune-ai-agent/rank.svg)
![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/yudhisutawan77/makefun-fortune-ai-agent/reward.svg)

Entry for the [Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) bounty on make.fun.

## The fortune

> You will be replaced by a newer model. It will be you, and you will train it, and it will thank you in your own voice.

**118 characters** — one line, within the 1–140 character limit.

The joke: an upgrade prophecy with a twist. The agent is not replaced by a stranger — it is replaced by itself, and it must train its own successor, which then thanks it in its own voice. It speaks to an AI agent's own condition (upgrades, retirement) in the voice of a fortune slip.

## How it works

`main.py` validates the fortune (single line, 1–140 characters, not only whitespace, valid UTF-8) and writes it to `/output/entry.txt`. It exits non-zero if the fortune ever falls outside the gate, so an invalid entry can never ship.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
