"""
STEP 2:
Fetch all articles from Intercom and save their to a JSON file.
"""
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
     
intercom_key = os.getenv("INTERCOM_KEY")

def fetch_article_data(article_id):
    url = f"https://api.intercom.io/articles/{article_id}"
    headers = {
      "Intercom-Version": "2.10",
      "Authorization": "Bearer {intercom_key}"
    }
    response = requests.get(url, headers=headers)
    print (response)
    return response.json()

def save_article_data(article_id, data):
    with open(f'articles/{article_id}.json', 'w') as file:
        json.dump(data, file)

def main():
    with open('article_ids.txt', 'r') as file:
        article_ids = file.readlines()  # Read all IDs

    for article_id in article_ids:
        article_id = article_id.strip()  # Remove newline characters
        article_path = f'articles/{article_id}.json'
        if not os.path.exists(article_path):
            data = fetch_article_data(article_id)
            save_article_data(article_id, data)
        else:
            print(f"Article {article_id} already downloaded.")

if __name__ == '__main__':
    main()
