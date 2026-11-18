"""Example: run NPI Registry Scraper – Doctor & Dentist Leads (No 1,200 Cap) on Apify and print results.
Store page: https://apify.com/dedicated_crest/npi-healthcare-provider-leads
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "specialties": [
        "Dentist"
    ],
    "states": [
        "CA"
    ],
    "cities": [
        "San Diego, CA"
    ],
    "maxItems": 50
}

run = client.actor("dedicated_crest/npi-healthcare-provider-leads").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
