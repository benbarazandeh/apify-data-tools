"""Example: run UK Companies House: New Company Leads, Officers and Filings on Apify and print results.
Store page: https://apify.com/dedicated_crest/uk-companies-house-leads
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "sicCodes": ["62"],
    "incorporatedWithinDays": 31,
    "excludeDormant": True,
    "maxItems": 20
}

run = client.actor("dedicated_crest/uk-companies-house-leads").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
