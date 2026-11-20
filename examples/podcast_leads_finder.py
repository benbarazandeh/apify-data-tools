"""Example: run Podcast Scraper – Apple Podcasts Search & Host Email Leads on Apify and print results.
Store page: https://apify.com/dedicated_crest/podcast-leads-finder
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "searchTerms": ["b2b marketing"],
    "activeWithinDays": 60,
    "maxItems": 20
}

run = client.actor("dedicated_crest/podcast-leads-finder").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
