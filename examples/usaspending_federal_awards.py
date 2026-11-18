"""Example: run USAspending Scraper – Federal Contracts & Grant Awards on Apify and print results.
Store page: https://apify.com/dedicated_crest/usaspending-federal-awards
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "awardTypes": [
        "contracts"
    ],
    "keywords": [
        "artificial intelligence"
    ],
    "daysBack": 30,
    "maxItems": 25
}

run = client.actor("dedicated_crest/usaspending-federal-awards").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
