"""Example: run Medium Scraper: Articles by Tag, Author and Publication on Apify and print results.
Store page: https://apify.com/dedicated_crest/medium-articles-scraper
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "tags": [
        "artificial-intelligence"
    ],
    "maxItems": 30,
    "proxyConfiguration": {
        "useApifyProxy": True,
        "apifyProxyGroups": [
            "RESIDENTIAL"
        ]
    }
}

run = client.actor("dedicated_crest/medium-articles-scraper").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
