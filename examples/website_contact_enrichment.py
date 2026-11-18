"""Example: run Website Contact Scraper – Emails, Phones & Socials on Apify and print results.
Store page: https://apify.com/dedicated_crest/website-contact-enrichment
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "websites": [
        "stripe.com",
        "https://www.defenseplumbing.com/",
        "griffon.paris"
    ],
    "maxItems": 100
}

run = client.actor("dedicated_crest/website-contact-enrichment").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
