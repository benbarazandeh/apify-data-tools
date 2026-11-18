"""Example: run Quora Scraper: Questions, Answers and Profiles (No Login) on Apify and print results.
Store page: https://apify.com/dedicated_crest/quora-questions-answers-scraper
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "questionUrls": [
        "https://www.quora.com/How-do-I-learn-Python-3",
        "https://www.quora.com/What-is-the-best-way-to-save-money"
    ],
    "profileUrls": [
        "https://www.quora.com/profile/Jimmy-Wales"
    ],
    "maxQuestions": 5,
    "maxItems": 30,
    "proxyConfiguration": {
        "useApifyProxy": True,
        "apifyProxyGroups": [
            "RESIDENTIAL"
        ],
        "apifyProxyCountry": "US"
    }
}

run = client.actor("dedicated_crest/quora-questions-answers-scraper").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
