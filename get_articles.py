"""
STEP 1:
Get all articles ID from Intercom and save their IDs to a file.
"""
import requests
import os
from dotenv import load_dotenv

load_dotenv()
     
intercom_key = os.getenv("INTERCOM_KEY")

def fetch_all_article_ids():
    page = 1
    article_ids = []
    while True:
        url = f"https://api.intercom.io/articles?page={page}"
        headers = {
          "Intercom-Version": "2.10",
          "Authorization": "Bearer {intercom_key}"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        new_ids = [article['id'] for article in data.get('data', [])]
        if not new_ids:
            break
        article_ids.extend(new_ids)
        page += 1
    with open('article_ids.txt', 'w') as file:
        for article_id in article_ids:
            file.write(f"{article_id}\n")

if __name__ == '__main__':
    fetch_all_article_ids()
