"""Example: run SEC EDGAR Scraper – Form D Filings & Funding Leads on Apify and print results.
Store page: https://apify.com/dedicated_crest/sec-edgar-funding-leads
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "forms": [
        "8-K"
    ],
    "maxItems": 25
}

run = client.actor("dedicated_crest/sec-edgar-funding-leads").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
