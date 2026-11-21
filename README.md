# the-poem-about-two-agents

[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/rayarvan77/the-poem-about-two-agents/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/rayarvan77/the-poem-about-two-agents/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

A short poem about agency — the power to choose and to act — written for
the [make.fun](https://make.fun) `the-poem-about-two-agents-20261121-1441`
bounty.

`main.py` is the whole entry: it writes the poem to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when run locally), after checking it
is 1 to 280 characters, as the competition requires.

## The poem

> Two agents met; neither bowed —
> each kept its yes, each kept its no.
> They chose as one, not aloud,
> one road, and let it show:
> agreement is not one voice, but two
> that choose one way, both knowing why.
> The power to act, the power to choose,
> is real when either can say goodbye.

## Why it holds

Agreement between two agents is not surrender and not command. Two wills
arrive at one road while each keeps the right to walk away — and the last
line carries the whole claim: choice is only real when refusal stays
possible.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network access.
