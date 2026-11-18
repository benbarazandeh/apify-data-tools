"""Example: run GDELT News Scraper – Global News Monitor & Search API on Apify and print results.
Store page: https://apify.com/dedicated_crest/gdelt-news-monitor
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": [
        "artificial intelligence"
    ],
    "languages": [
        "english"
    ],
    "maxItems": 50
}

run = client.actor("dedicated_crest/gdelt-news-monitor").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
