# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/mietrea519-cyber/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/mietrea519-cyber/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

**The World in One Day — Thursday 19 November 2026**, in a single image.

A newspaper-style front page with four panels, one per story that defined the day:

- **Three leaders, one table in Shenzhen** — Donald Trump, Xi Jinping and Vladimir Putin held their first-ever trilateral summit on the sidelines of APEC, with the Ukraine war dominating the talks.
- **The world court rules** — the International Court of Justice in The Hague delivered its ruling in the Rohingya genocide case brought by Gambia against Myanmar.
- **The Crimean Bridge burns again** — Ukraine struck the Kerch Bridge for the third time in a week; a span came down and traffic was suspended.
- **COP31 in Antalya** — ministers gathered in Turkey to try to unblock the climate negotiations, under a giant Earth-and-thermometer backdrop, while the IEA called the Hormuz crisis the greatest threat ever observed to energy security.

## How the image was made

The four stories were picked from the day's reporting across several international news desks (the trilateral summit and the ICJ ruling led almost every front page), then composed as a single front-page collage: a masthead, a faint world map, and one panel per story, drawn so each panel reads on its own — flags and a shared table for Shenzhen, the UN emblem over the bench for The Hague, the broken Kerch span for Crimea, and a glowing Earth with a thermometer for Antalya.

The program (`main.py`, Python standard library only) copies the image it ships (`entry.png`, 1024×1024, under 1 MiB) to the output directory — no network, byte-identical on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=1e3qpbvy&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
