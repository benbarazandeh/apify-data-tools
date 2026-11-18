"""Example: run FMCSA Trucking Scraper – New Carrier Leads, USDOT/MC Census on Apify and print results.
Store page: https://apify.com/dedicated_crest/fmcsa-trucking-carrier-leads
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "states": [
        "TX"
    ],
    "cities": [
        "Dallas, TX"
    ],
    "maxItems": 25
}

run = client.actor("dedicated_crest/fmcsa-trucking-carrier-leads").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
