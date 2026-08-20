---
name: autonomous-crisis-analyst
description: Autonomously search for emerging global crises or macroeconomic risks, score them to find the highest-signal topic, and produce a complete award-winning Substack analysis with dark-mode data visualization. Use when the user wants a new, highly relevant geopolitical or economic analysis without providing a specific topic.
license: Complete terms in LICENSE.txt
---

# Autonomous Crisis Analyst

This skill enables you to act as an autonomous editorial director and lead analyst. It guides you through discovering emerging global topics, selecting the best one, and executing a complete research-to-publication workflow for a Substack audience.

## Phase 1: Topic Discovery & Selection

Do not ask the user for a topic. Find one yourself.

1. **Broad Search**: Use the `search` tool (type `news` or `info`) to scan for emerging macroeconomic, geopolitical, or systemic risks in the current year.
2. **Topic Scoring**: Evaluate 3-4 potential topics against this rubric (0-10 points each):
   - *Systemic Impact*: Does this threaten global supply chains, financial stability, or democratic governance?
   - *Data Availability*: Are there hard numbers (IMF, BIS, World Bank) to visualize?
   - *Counter-Narrative*: Does this challenge mainstream assumptions (e.g., "debt is fine," "tech always creates jobs")?
3. **Selection**: Pick the highest-scoring topic and inform the user of your choice via an `info` message.

## Phase 2: Deep Research & Visualization

1. **Deep Research**: Conduct targeted searches on the selected topic. Gather specific data points suitable for charting.
2. **Data Visualization**: Generate a professional dark-mode Python visualization.
   - Use the template located at `/home/ubuntu/skills/autonomous-crisis-analyst/templates/dark_mode_viz_template.py` as your starting point.
   - **Style Rules**: Background `#0d1117`, Panel `#161b22`, Text `#e8e8e8`. Accent colors: Gold (`#f0b429`), Teal (`#1a9e8f`), Red (`#e05252`).
   - Save as a high-res PNG.

## Phase 3: Article Drafting (Anti-AI Slop)

Write the article as a brilliant human expert.

- **Banned Words**: delve, intricate, nuance, realm, moreover, catalyst, comprehensive, significant, enhance, crucial, vital, ever-evolving, tapestry, unlock the power of, revolutionize, game-changer, unparalleled, it is important to note that.
- **Formatting**: NEVER use double asterisks (`**`) for bold emphasis in the body text.
- **Structure**:
  - Social media hook.
  - Meta title and description.
  - Substack body text (short paragraphs, pull-quotes).
  - Embed the generated visualization.
  - Substack CTA (subscribe/comment).
  - FAQ section.
  - APA 7 References.

## Phase 4: Quality Assurance

Before delivering the final Markdown file, you MUST run this exact bash command:

```bash
grep -iE "delve|intricate|nuance|realm|moreover|catalyst|comprehensive|significant|enhance|crucial|vital|ever-evolving|tapestry|unlock the power|revolutionize|game-changer|unparalleled|it is important to note|\*\*" /path/to/article.md
```

If it returns any hits, edit the file to remove them before delivering the result.
