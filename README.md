# Apify data tools

Examples, n8n workflows, and MCP setup for the public [Apify](https://apify.com) Actors by [dedicated_crest](https://apify.com/dedicated_crest). Titles and one-line descriptions below are from the Apify Store as of 18 Nov 2026.

Runs are billed to your own Apify account at each Actor's Store price. A new account can start on the Free plan ($5 of monthly platform credit, no credit card). Lower `maxItems` to keep tests cheap.

## Actors

| Actor | What it does | Example | Console |
|---|---|---|---|
| [App Store Reviews Scraper – Apple iOS Reviews, 150+ Countries](https://apify.com/dedicated_crest/app-store-reviews-scraper) | Scrape Apple App Store reviews for any iOS app: rating, text, version, date, author in 150+ countries. Filter by stars, date, keywords. $0.20 per 1,000 reviews. | [`examples/app_store_reviews_scraper.py`](examples/app_store_reviews_scraper.py) | [Open with example input](https://console.apify.com/actors/3noFaLjW11eAPs6AD/input) |
| [Bluesky Scraper – Posts Search, Profiles & Leads](https://apify.com/dedicated_crest/bluesky-posts-profiles-search) | Scrape Bluesky: search posts by keyword or hashtag with date and language filters, plus profiles with bio links, emails, domains and followers. Official API, $1/1,000. | [`examples/bluesky_posts_profiles_search.py`](examples/bluesky_posts_profiles_search.py) | [Open with example input](https://console.apify.com/actors/GxV2kUqe9bPaEXVfL/input) |
| [Bulk WHOIS & DNS Lookup – Domain Age, RDAP, Email Provider](https://apify.com/dedicated_crest/domain-whois-dns-intel) | Bulk WHOIS/RDAP & DNS lookup: registrar, creation & expiry date, domain age, availability, MX/SPF/DMARC, email provider, SaaS stack, website. $3/1,000 domains. | [`examples/domain_whois_dns_intel.py`](examples/domain_whois_dns_intel.py) | [Open with example input](https://console.apify.com/actors/mmRcNNkyc8v0EsnqP/input) |
| [Capterra Reviews Scraper: Ratings, Pros & Cons (No Login)](https://apify.com/dedicated_crest/capterra-reviews-scraper) | Scrape Capterra software reviews: star ratings, sub-scores, pros, cons, reviewer job title and dates. Filter by stars and date. $1 per 1,000 reviews. | [`examples/capterra_reviews_scraper.py`](examples/capterra_reviews_scraper.py) | [Open with example input](https://console.apify.com/actors/PRqRKsgfth2IKgJGG/input) |
| [Career Site Jobs API – Greenhouse, Lever, Workday, Ashby](https://apify.com/dedicated_crest/ats-career-jobs-scraper) | Scrape all open jobs from company career sites: Greenhouse, Lever, Ashby, Workday, Workable, SmartRecruiters. Salary, remote, apply link. $2/1,000 jobs. | [`examples/ats_career_jobs_scraper.py`](examples/ats_career_jobs_scraper.py) | [Open with example input](https://console.apify.com/actors/WwnJod6qT890gGYfj/input) |
| [FMCSA Trucking Scraper – New Carrier Leads, USDOT/MC Census](https://apify.com/dedicated_crest/fmcsa-trucking-carrier-leads) | Official FMCSA census scraper: new trucking & motor carriers by state, fleet size, USDOT date, phone, email, MC & authority. For brokers, insurance, factoring. | [`examples/fmcsa_trucking_carrier_leads.py`](examples/fmcsa_trucking_carrier_leads.py) | [Open with example input](https://console.apify.com/actors/OYGIEL4x0GmbUh4rc/input) |
| [GDELT News Scraper – Global News Monitor & Search API](https://apify.com/dedicated_crest/gdelt-news-monitor) | Scrape & monitor global news via the official GDELT API: keywords, sites, country, language, tone. Deduped, no API key. Google Alerts alternative, $2/1,000. | [`examples/gdelt_news_monitor.py`](examples/gdelt_news_monitor.py) | [Open with example input](https://console.apify.com/actors/C0gVEJJhVsTMIFJmq/input) |
| [Grants.gov Scraper – Federal Grants & Nonprofit Grants Finder](https://apify.com/dedicated_crest/grants-gov-opportunity-finder) | Search federal grants and nonprofit grants on Grants.gov by keyword, agency, CFDA and eligibility. Deadlines, award amounts, contacts and new-grant alerts. $3/1,000. | [`examples/grants_gov_opportunity_finder.py`](examples/grants_gov_opportunity_finder.py) | [Open with example input](https://console.apify.com/actors/imbcI522UkGM5yadr/input) |
| [Hacker News Scraper – Who Is Hiring Jobs, Search & Comments](https://apify.com/dedicated_crest/hacker-news-search-hiring) | Scrape Hacker News: parsed Who is hiring job posts (company, role, remote, salary), story & comment search, top/new/Show HN feeds. Official API, $3/1,000. | [`examples/hacker_news_search_hiring.py`](examples/hacker_news_search_hiring.py) | [Open with example input](https://console.apify.com/actors/UtYvToTq7p3Ay2nRf/input) |
| [Local Business Leads – OpenStreetMap, Emails & Phones](https://apify.com/dedicated_crest/osm-local-business-leads) | Get local business leads by category & city: name, address, phone, website, hours, coordinates + emails from business websites. OpenStreetMap data, $3/1,000. | [`examples/osm_local_business_leads.py`](examples/osm_local_business_leads.py) | [Open with example input](https://console.apify.com/actors/CaXtHyEnLdr2XQOD3/input) |
| [Medium Scraper: Articles by Tag, Author and Publication](https://apify.com/dedicated_crest/medium-articles-scraper) | Scrape Medium articles by tag, author, publication or article URL using public RSS feeds: title, author, dates, tags, summary or full text, claps, responses, and reading time. | [`examples/medium_articles_scraper.py`](examples/medium_articles_scraper.py) | [Open with example input](https://console.apify.com/actors/i2aJxAc59YbSECM47/input) |
| [NPI Registry Scraper – Doctor & Dentist Leads (No 1,200 Cap)](https://apify.com/dedicated_crest/npi-healthcare-provider-leads) | Official NPPES NPI Registry scraper: US doctors, dentists & clinics, past the 1,200 cap. Specialty, address, phone, fax, owner. State, city, ZIP. $1/1,000. | [`examples/npi_healthcare_provider_leads.py`](examples/npi_healthcare_provider_leads.py) | [Open with example input](https://console.apify.com/actors/AeZTbhypXKAXC4S18/input) |
| [Quora Scraper: Questions, Answers and Profiles (No Login)](https://apify.com/dedicated_crest/quora-questions-answers-scraper) | Scrape public Quora questions, answers with views and upvotes, and user profiles without login. $1.90 per 1,000 results, proxy included. | [`examples/quora_questions_answers_scraper.py`](examples/quora_questions_answers_scraper.py) | [Open with example input](https://console.apify.com/actors/4nwccBhvYJ1z8DIGC/input) |
| [SEC EDGAR Scraper – Form D Filings & Funding Leads](https://apify.com/dedicated_crest/sec-edgar-funding-leads) | SEC EDGAR scraper: Form D filings with amount raised, industry, phone and executives, plus EDGAR full-text search (8-K, 10-K, S-1, Form 4). Official SEC data, no API key. | [`examples/sec_edgar_funding_leads.py`](examples/sec_edgar_funding_leads.py) | [Open with example input](https://console.apify.com/actors/hkA76yVNeOzRkV2qH/input) |
| [Substack Scraper – Newsletter Posts, Search & Publication Info](https://apify.com/dedicated_crest/substack-posts-newsletter-scraper) | Scrape Substack posts by newsletter URL or keyword: title, date, author, likes, comments, restacks, free/paid flag and publication info. No login. | [`examples/substack_posts_newsletter_scraper.py`](examples/substack_posts_newsletter_scraper.py) | [Open with example input](https://console.apify.com/actors/QdGppPjXeQ4APuMFP/input) |
| [USAspending Scraper – Federal Contracts & Grant Awards](https://apify.com/dedicated_crest/usaspending-federal-awards) | USAspending scraper for federal contracts and grant awards: recipient, UEI, NAICS, agency, set-aside, amount. Official USAspending.gov API, no key. $2 per 1,000 awards. | [`examples/usaspending_federal_awards.py`](examples/usaspending_federal_awards.py) | [Open with example input](https://console.apify.com/actors/1gBWYbXAbdVPHOBz7/input) |
| [Website Contact Scraper – Emails, Phones & Socials](https://apify.com/dedicated_crest/website-contact-enrichment) | Extract emails, phones, LinkedIn, Facebook, Instagram & X profiles and contact pages from lists of company websites. robots.txt-friendly, $2 per 1,000 websites. | [`examples/website_contact_enrichment.py`](examples/website_contact_enrichment.py) | [Open with example input](https://console.apify.com/actors/qPFqWrhmM6FRkPYvd/input) |

## Use them as MCP tools

[Apify's MCP server](https://docs.apify.com/mcp) can load one or more of these Actors as tools in Claude, Cursor, or any other MCP client. On first use, sign in to Apify with OAuth, or pass an Apify API token as `Authorization: Bearer <your-token>`.

Connect a single Actor with:

```
https://mcp.apify.com?tools=dedicated_crest/<actor>
```

For example:

- Grants: `https://mcp.apify.com?tools=dedicated_crest/grants-gov-opportunity-finder`
- GDELT: `https://mcp.apify.com?tools=dedicated_crest/gdelt-news-monitor`
- FMCSA: `https://mcp.apify.com?tools=dedicated_crest/fmcsa-trucking-carrier-leads`

To load all three at once:

```
https://mcp.apify.com?tools=dedicated_crest/grants-gov-opportunity-finder,dedicated_crest/gdelt-news-monitor,dedicated_crest/fmcsa-trucking-carrier-leads
```

Configurator and docs: [mcp.apify.com](https://mcp.apify.com) and [docs.apify.com/mcp](https://docs.apify.com/mcp).

### Example prompts

**Grants.** Find open Grants.gov opportunities for 501(c)(3) nonprofits about community health, and show the deadline, award ceiling, and agency contact for each one.

**GDELT.** Search worldwide English-language news from the last 24 hours about artificial intelligence, and return each article's headline, URL, outlet, country, and tone.

**FMCSA.** List active motor carriers in Dallas, TX that have a phone number, and include USDOT, MC number, fleet size, safety rating, and authority status.

## n8n workflows

Ready-to-import workflow JSON lives in [`examples/n8n`](examples/n8n). See that folder's [README](examples/n8n/README.md) for setup notes.

- [Log new FMCSA carriers daily](examples/n8n/fmcsa-new-carriers-daily.json) — approved as [n8n template 22715](https://n8n.io/workflows/22715)
- [Score new Grants.gov grants with AI](examples/n8n/grants-gov-ai-matcher.json) — approved as [n8n template 22191](https://n8n.io/workflows/22191)
- [Monitor GDELT brand mentions daily](examples/n8n/gdelt-brand-mentions-daily.json) — submitted as [n8n template 22960](https://n8n.io/workflows/22960) (under review when this repo was published)

## Python examples

```bash
pip install -r requirements.txt
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python examples/gdelt_news_monitor.py
```

Each script starts the Actor with a small example input (the same kind of prefill the Store page uses) and prints the dataset items. Do not put your token in the script; keep it in the environment variable.

## License

MIT
