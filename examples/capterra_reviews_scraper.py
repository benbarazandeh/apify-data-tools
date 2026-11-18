"""Example: run Capterra Reviews Scraper: Ratings, Pros & Cons (No Login) on Apify and print results.
Store page: https://apify.com/dedicated_crest/capterra-reviews-scraper
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "productUrls": [
        "https://www.capterra.com/p/135003/Slack/"
    ],
    "maxReviewsPerProduct": 50,
    "maxItems": 50
}

run = client.actor("dedicated_crest/capterra-reviews-scraper").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
