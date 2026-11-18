"""Example: run Grants.gov Scraper – Federal Grants & Nonprofit Grants Finder on Apify and print results.
Store page: https://apify.com/dedicated_crest/grants-gov-opportunity-finder
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keyword": "artificial intelligence",
    "maxItems": 20
}

run = client.actor("dedicated_crest/grants-gov-opportunity-finder").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
