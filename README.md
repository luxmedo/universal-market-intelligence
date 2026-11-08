# Universal Market Intelligence

Reusable market research skill for **Claude Code** and **OpenAI Codex**. Works across digital products, physical retail, SaaS, services and marketplaces.

## Installation

### Claude Code (project-level)
```bash
git clone https://github.com/luxmedo/universal-market-intelligence.git
mkdir -p .claude/skills/universal-market-intelligence
cp -R universal-market-intelligence/{SKILL.md,references,templates,scripts} .claude/skills/universal-market-intelligence/
```

### Codex (user-level)
```bash
git clone https://github.com/luxmedo/universal-market-intelligence.git
mkdir -p ~/.agents/skills/universal-market-intelligence
cp -R universal-market-intelligence/{SKILL.md,references,templates,scripts} ~/.agents/skills/universal-market-intelligence/
```

The commands above are for bash (Linux, macOS, WSL). On Windows PowerShell, use Copy-Item -Recurse and appropriate paths. Alternatively, paste this repository URL into Claude Code or Codex and ask it to inspect and install the skill into its supported skills directory.

## Example prompt
"Use universal-market-intelligence to analyze [market] in [country]. Include demand, trends, competitor pricing, customer needs, unit economics, risks, and a 30-day validation plan."

## What's included
- SKILL.md: complete research workflow
- references/sources.md: lawful data sources and fallbacks
- references/scoring.md: opportunity scoring rubric
- templates/report.md: structured report
- scripts/unit_economics.py: offline margin calculator
- tests/test_unit_economics.py: Python tests

## Limitations
No paid API credentials or automatic access to eRank, EverBee, Similarweb or Google Ads are bundled. Live information requires available browsing tools, official APIs, or data exports. This skill never claims private marketplace sales data is public.
