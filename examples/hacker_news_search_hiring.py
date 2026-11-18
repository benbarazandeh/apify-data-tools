"""Example: run Hacker News Scraper – Who Is Hiring Jobs, Search & Comments on Apify and print results.
Store page: https://apify.com/dedicated_crest/hacker-news-search-hiring
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "mode": "whoIsHiring",
    "keywords": [
        "engineer"
    ],
    "maxItems": 50
}

run = client.actor("dedicated_crest/hacker-news-search-hiring").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
