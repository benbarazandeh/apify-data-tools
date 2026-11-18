# n8n workflows

Import in n8n with **Workflows → Import from File**. After import, attach your own credentials and replace the placeholders (`you@example.com`, `YOUR_SHEET_ID`, and your Apify token in a Header Auth credential). None of these files contain a real API token, spreadsheet ID, or personal email.

Runs are billed to your own Apify account at each actor's Store price. Keep `maxItems` modest so the `run-sync-get-dataset-items` call can finish within the 5-minute limit.

## Log new FMCSA carriers daily, dedupe in Sheets, and email a digest

- File: [`fmcsa-new-carriers-daily.json`](fmcsa-new-carriers-daily.json)
- Actor: [FMCSA Trucking Scraper](https://apify.com/dedicated_crest/fmcsa-trucking-carrier-leads)
- Status: approved on the n8n template library as [workflow 22715](https://n8n.io/workflows/22715)
- What it does: every morning it reads USDOT numbers already in your Google Sheet, runs the actor for recently added carriers in the state you set, keeps only those with active authority and a phone or email, skips anything already logged, appends the new rows, and emails a short digest (or an all-clear if nothing new qualified). A failed actor call or workflow error sends a warning email instead of failing silently.

## Score new Grants.gov grants with AI, log to Sheets, and email top matches

- File: [`grants-gov-ai-matcher.json`](grants-gov-ai-matcher.json)
- Actor: [Grants.gov Scraper](https://apify.com/dedicated_crest/grants-gov-opportunity-finder)
- Status: approved on the n8n template library as [workflow 22191](https://n8n.io/workflows/22191)
- What it does: every morning it fetches newly posted and forecasted federal opportunities for your keyword, skips grants already in your sheet, scores each new grant 0–10 against the organization profile in the settings node, logs every new grant, and emails a digest of matches at or above your minimum score.
- Setup notes: this template uses the `@apify/n8n-nodes-apify` community node and an OpenAI (or other LangChain) chat model, plus Google Sheets and Gmail OAuth2. Install the Apify node before running it. Edit the sample organization profile and `you@example.com` before you activate the workflow.

## Monitor GDELT brand mentions daily, dedupe in Sheets, and email a digest

- File: [`gdelt-brand-mentions-daily.json`](gdelt-brand-mentions-daily.json)
- Actor: [GDELT News Scraper](https://apify.com/dedicated_crest/gdelt-news-monitor)
- Status: submitted to the n8n template library as [workflow 22960](https://n8n.io/workflows/22960) (under review at the time this repo was published)
- What it does: every morning it reads article URLs already in your Google Sheet, runs the actor for the keywords, languages, optional countries, and time span you set, can label tone and optionally keep only a chosen tone, skips URLs already logged, appends the new rows, and emails a short digest (or an all-clear). A failed actor call or workflow error sends a warning email.
