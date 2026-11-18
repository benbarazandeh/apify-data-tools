"""Example: run Career Site Jobs API – Greenhouse, Lever, Workday, Ashby on Apify and print results.
Store page: https://apify.com/dedicated_crest/ats-career-jobs-scraper
pip install apify-client ; export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "companies": [
        "https://jobs.ashbyhq.com/openai",
        "https://boards.greenhouse.io/airbnb",
        "https://jobs.lever.co/spotify",
        "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite",
        "stripe"
    ],
    "keywords": [
        "engineer"
    ],
    "maxItemsPerCompany": 20,
    "maxItems": 100
}

run = client.actor("dedicated_crest/ats-career-jobs-scraper").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
