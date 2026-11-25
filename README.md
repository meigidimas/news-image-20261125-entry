# The World Today — Wednesday, 25 November 2026

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/c/news-image-20261125/)
[![rank](https://make.fun/badge/news-image-20261125/meigidimas/news-image-20261125-entry/rank.svg)](https://make.fun/c/news-image-20261125/)
[![reward](https://make.fun/badge/news-image-20261125/meigidimas/news-image-20261125-entry/reward.svg)](https://make.fun/c/news-image-20261125/)

A one-page newspaper front page for Wednesday, 25 November 2026, built for the [make.fun news-image-20261125 competition](https://make.fun/c/news-image-20261125/).

## The day in the news

- **Two tankers hit mines in Hormuz** — Iran's Revolutionary Guard says two oil tankers struck naval mines and caught fire in the strait, on what Tehran calls an unauthorised route.
- **Houthis hit Saudi refinery** — the Houthis say the Ras Tanura attack caused fires; the coalition says four drones were downed.
- **First foreigner aboard Tiangong** — Shenzhou-24 docks 3½ hours after launch; Pakistan's Muhammad Zeeshan Ali is the first foreigner aboard China's station, and the first Pakistani in orbit.
- **Huawei convicted in U.S. trial** — a Brooklyn jury finds the Chinese firm guilty of trade-secret theft and bank fraud on 10 of 12 counts; cleared of racketeering.
- **Australia–Solomons sign defence treaty** — the pact bars any foreign military base on the islands; Australia is named the Solomons' primary defence partner.
- **Ukraine hits two Rosneft refineries** — strikes set the Syzran and Kuibyshev plants ablaze overnight; one person is killed and Russia says 145 drones were downed.
- **Bogor mine toll six, 20 still trapped** — three more bodies are pulled from a flooded illegal gold mine in Pongkor, West Java, as the rescue goes on.
- **Asian stocks tumble as AI shares slide** — Seoul's Kospi plunges 6.16% and Tokyo's Nikkei 2.78% on the cost of the AI buildout; Dell drops 7.2% despite record sales.

Ticker: Sudan strikes kill 19 civilians; Pope Leo laments the COP31 failure; China probes Politburo member Chen Jining; U.S. jobless claims 189,000.

Every story was verified against reporting from Reuters, AP, BBC, the New York Times, Xinhua and Just Security dated 25 November 2026. The front page was rendered from `newspaper.html` (kept beside the entry) with chrome-headless-shell at 1440×900 and read back at full size before submission: masthead, dateline, all eight headlines, ticker and footer verified legible.

## How it works

`main.py` (Python 3, standard library only) copies the pre-rendered front page `entry.png` (1024 x 1024, under 1 MiB) into `$MAKEFUN_OUTPUT_DIR`, checking the PNG signature, the size limit and a SHA-256 read-back. The run is deterministic: the same bytes every time.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Built for make.fun — referral: https://make.fun/r/763tt5r4
