"""Example: run Bluesky Scraper – Posts Search, Profiles & Leads on Apify and print results.
Store page: https://apify.com/dedicated_crest/bluesky-posts-profiles-search
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "mode": "posts",
    "queries": [
        "#opensource"
    ],
    "maxItems": 50
}

run = client.actor("dedicated_crest/bluesky-posts-profiles-search").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
