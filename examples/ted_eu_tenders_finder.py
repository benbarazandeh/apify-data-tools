"""Example: run TED Scraper – EU Public Tenders & Contract Awards Finder on Apify and print results.
Store page: https://apify.com/dedicated_crest/ted-eu-tenders-finder
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": ["software"],
    "countries": ["DE", "FR"],
    "maxItems": 20
}

run = client.actor("dedicated_crest/ted-eu-tenders-finder").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
