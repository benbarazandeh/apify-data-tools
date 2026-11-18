"""Example: run App Store Reviews Scraper – Apple iOS Reviews, 150+ Countries on Apify and print results.
Store page: https://apify.com/dedicated_crest/app-store-reviews-scraper
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "apps": [
        "https://apps.apple.com/us/app/instagram/id389801252",
        "duolingo"
    ],
    "countries": [
        "us",
        "gb"
    ],
    "maxReviewsPerApp": 50
}

run = client.actor("dedicated_crest/app-store-reviews-scraper").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
