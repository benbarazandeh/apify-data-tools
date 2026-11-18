"""Example: run Local Business Leads – OpenStreetMap, Emails & Phones on Apify and print results.
Store page: https://apify.com/dedicated_crest/osm-local-business-leads
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "categories": [
        "cafe"
    ],
    "latitude": "30.2672",
    "longitude": "-97.7431",
    "radiusKm": 1,
    "maxItems": 10
}

run = client.actor("dedicated_crest/osm-local-business-leads").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
