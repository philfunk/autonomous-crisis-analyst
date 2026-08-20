# Autonomous Crisis Analyst

A reusable skill that finds an emerging geopolitical or macroeconomic risk topic on its own, ranks candidate themes by analytical value, and produces a research-grounded Substack article with a dark-mode data visualization.

## What It Produces

The skill turns an open prompt such as “find a new topic and write an analysis” into a full editorial package:

| Stage | Output |
|---|---|
| Topic discovery | Three to four current candidate topics and a scored choice |
| Evidence collection | Primary-source research, hard data, and attributable claims |
| Data storytelling | A high-resolution, dark-mode multi-panel PNG visualization |
| Long-form analysis | A Substack-ready article with a hook, narrative argument, FAQ, CTA, and APA 7 references |
| Editorial QA | A banned-phrase and formatting scan before delivery |

## Selection Model

The skill ranks each possible topic from 0 to 30, using three equally weighted criteria.

| Criterion | Question |
|---|---|
| Systemic impact | Could this topic materially affect global supply chains, financial stability, security, or democratic governance? |
| Data availability | Is there current, authoritative, chart-ready evidence from institutions such as the IMF, BIS, World Bank, OECD, IEA, or central banks? |
| Counter-narrative | Does the topic expose a weak assumption or a neglected second-order risk in the usual public debate? |

The winner is the highest-scoring theme. The analysis should make its selection logic explicit, rather than treating a newsworthy topic as automatically consequential.

## Installation

Add `SKILL.md` through the Manus Skills interface, or copy the full folder to the local skills directory:

```bash
cp -R autonomous-crisis-analyst /home/ubuntu/skills/
```

## Usage

Use a natural-language prompt. The user does not need to supply a topic.

```text
Find the highest-signal global risk topic this week and write an award-winning Substack analysis with one data visualization.
```

The skill will scan current news and research, score candidate topics, select one, research it, generate the visualization, write the article, and run editorial quality checks.

## Repository Structure

```text
.
├── SKILL.md
├── templates/
│   └── dark_mode_viz_template.py
├── requirements.txt
├── LICENSE
└── README.md
```

`templates/dark_mode_viz_template.py` is the reference implementation for the visual language used in the project: dark navy canvas, gold/teal/red accents, readable annotations, recession or event shading, and a multi-panel GridSpec layout. Adapt the data series, labels, sources, and panel logic to the selected topic. Do not present illustrative values as factual data; replace all data with sourced values before publication.

## Editorial Principles

The analysis must retain a clear distinction between fact, interpretation, and scenario. It should not forecast a crisis with certainty, advocate violence, or use unexplained alarmist claims. It should cite factual claims to the original source wherever possible and give readers a useful framework rather than merely a catalogue of threats.

## License

Released under the MIT License. See [LICENSE](LICENSE).

## Attribution

Created as a reusable analysis workflow for Manus.

## Disclaimer

This project supports research and editorial analysis. It does not provide financial, legal, military, or investment advice.
