"""Example: run Substack Scraper – Newsletter Posts, Search & Publication Info on Apify and print results.
Store page: https://apify.com/dedicated_crest/substack-posts-newsletter-scraper
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "publicationUrls": [
        "https://www.lennysnewsletter.com"
    ],
    "maxPostsPerSource": 20
}

run = client.actor("dedicated_crest/substack-posts-newsletter-scraper").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
