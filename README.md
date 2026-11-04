# A consistency gate for document-extraction candidates

[NuMind](https://numind.ai/) builds specialist document-extraction models. This independent toy explores a small *post-extraction* question: if a system has several possible invoice JSON outputs, when should it emit one, and when should it abstain?

Run `python3 experiment.py` to reproduce `report.json` from [eight hand-authored candidates](fixtures.json). Selecting the first candidate matches the fixture's expected decision in **3/8** cases. Requiring arithmetic consistency (`sum(lines) + tax = total`) and agreement with an explicitly printed total, then accepting only a unique supported candidate, matches **8/8**, with **3 abstentions**.

No NuMind model, OCR engine, image, PDF, or API is evaluated. The candidates and expected decisions are written to exercise the rule, so these counts are **not accuracy results**. A next study could run real extraction outputs on held-out documents, then measure wrong-field rate, coverage after abstention, and human review cost.

Sources: [Station F Future 40 2026](https://stationf.co/news/future-40-2026), [NuMind](https://numind.ai/), [NuMind team](https://numind.ai/about).
