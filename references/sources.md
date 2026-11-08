# Market data sources and fallbacks

Use the most relevant lawful sources for the country and market, and verify current access rules.

- Search interest: Google Trends (relative index, not absolute search volume).
- Search volumes and ads: Google Ads Keyword Planner / API (may require account, permissions and quotas).
- Etsy: Etsy Open API where approved, official public listings, and user-provided licensed exports. Do not assume access to sales figures or eRank/EverBee.
- Competitors: official product pages, public pricing, public filings and reputable industry reports.
- Website traffic: Similarweb or comparable providers if licensed; third-party traffic numbers are estimates.
- Customers: permitted public reviews, interviews, surveys and communities; protect personal data.
- Physical markets: official statistics, trade reports, customs data where published.

Fallback: official permitted API -> public official information -> reputable third-party reports -> user-provided CSV -> mark unknown.

For every number, capture URL, date, geography, metric definition, whether measured or estimated, and confidence.
No CAPTCHA bypass, credential harvesting, stealth scraping, or rate-limit circumvention.
