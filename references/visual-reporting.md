# Visual Intelligence & Dashboard Design

## Goal
Every completed market analysis must produce a professional visual summary that makes findings understandable at a glance. Prefer a single polished dashboard plus a detailed written report.

## Required visual structure
1. Header: market, geography, date, research period, source coverage.
2. KPI cards: only measured or sourced metrics; otherwise label as estimate or unknown.
3. Demand & seasonality: time-series line chart when dated observations exist.
4. Competitor comparison: horizontal bar chart for comparable prices or other numeric metrics; comparison table when dimensions differ.
5. Price distribution: histogram or box plot only with enough actual price observations.
6. Unit economics: conservative/base/optimistic scenario bars or waterfall; prominently mark assumed inputs.
7. Risk & opportunity: labeled score bars or matrix with confidence and evidence gaps.
8. Decision: GO / TEST / NO-GO with explanation and 30-day validation steps.
9. Footnotes: source URLs, retrieval dates, currency, units, and methodology.

## Chart selection rules
- Time trends: line chart, sorted by date; never interpolate missing months without disclosure.
- Category comparison: horizontal bars with common units and a zero baseline.
- Part-to-whole: stacked bar; pie only when categories form a verified whole and there are few categories.
- Price vs demand: scatter plot only if paired observations exist.
- Financial scenarios: grouped bars or waterfall, with transparent assumptions.
- Do not mix currencies, periods, or measured and estimated series without labeling.
- Avoid 3D charts, misleading axes, invented percentages, or decorative graphics that obscure data.

## Visual design system
- Editorial, professional analytics dashboard; responsive 16:9 desktop layout and mobile-friendly stacked view.
- White/neutral canvas, strong typographic hierarchy, ample whitespace, accessible contrast.
- Use restrained, consistent color palette; not color alone for meaning.
- Explicit labels, units, legends, sources, and notes; large enough for mobile reading.
- Support the user's language and right-to-left layout for Arabic when practical.
- Make charts legible and information-dense, not ornamental.

## Output implementation
- Preferred: self-contained HTML dashboard with embedded SVG and no external scripts or remote assets. Use safe escaped text for user/source strings.
- If Python plotting is available: generate SVG/PNG charts and optionally PDF report.
- If the user explicitly asks for a static designed infographic, it may accompany charts, but numerical charts must remain programmatically data-driven.
- Save the dashboard as market-dashboard.html and include an export-ready market-data.json (or CSV) where possible.
- Render or open generated artifacts to check clipping, readability, data integrity and layout before delivery.
- If only a text interface is available, return a chart specification and Markdown tables rather than pretending an image exists.

## Data integrity checklist
- Every plotted value must trace to a cited observation or labeled scenario input.
- Never infer revenue from listing counts or search interest.
- Distinguish search interest index (0-100) from absolute search volume.
- Put unknown metrics in an Evidence Gaps section rather than filling with estimates.
- Make the recommendation conditional on the quality and recency of evidence.
