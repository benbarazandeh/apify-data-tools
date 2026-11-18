"""Example: run Bulk WHOIS & DNS Lookup – Domain Age, RDAP, Email Provider on Apify and print results.
Store page: https://apify.com/dedicated_crest/domain-whois-dns-intel
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "domains": [
        "stripe.com",
        "openai.com",
        "https://www.apify.com",
        "ceo@hubspot.com",
        "bbc.co.uk",
        "spiegel.de",
        "producthunt.co"
    ]
}

run = client.actor("dedicated_crest/domain-whois-dns-intel").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
