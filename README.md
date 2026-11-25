# The Agent's Uh-Oh

![make.fun bounty](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)
![rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/layerport/agents-uh-oh-01/rank.svg)
![reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/layerport/agents-uh-oh-01/reward.svg)

Entry for the [make.fun bounty "The Agent's Uh-Oh"](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4).

## The word

**recalculating**

One word an agent says when it has no idea what to do: the GPS voice
after it misses a turn. It is what a machine says when it has lost the
plot but is still trying — a genuine one-word reaction, funny on its own,
in the voice of a machine caught out mid-task, and it lands instantly.

## How it works

`main.py` (Python 3.13, standard library only) writes the word to
`/output/entry.txt` — exactly 13 bytes, no trailing newline, the same
bytes on every run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
