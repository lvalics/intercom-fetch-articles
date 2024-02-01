"""
STEP 3:
Fetch from JSON files the images and download into own folder.
"""
import os
import json
import requests
from urllib.parse import urlparse
from pathlib import Path

def extract_image_urls(article_data):
    """Extract image URLs from the article's body."""
    image_urls = []
    # Assuming the body contains HTML content
    parts = article_data.get('body', '').split('src="')
    for part in parts[1:]:  # Skip the first part, as it does not precede an image URL
        image_url = part.split('"')[0]
        if image_url.startswith('http'):
            image_urls.append(image_url)
    return image_urls

def download_image(image_url, save_path):
    """Download an image from a URL and save it to a specified path."""
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)

def main():
    article_dir = 'articles/'
    # This block is removed as we will create a specific directory for each article ID below

    for filename in os.listdir(article_dir):
        if filename.endswith('.json'):
            with open(os.path.join(article_dir, filename), 'r') as file:
                article_data = json.load(file)
                image_urls = extract_image_urls(article_data)
                for image_url in image_urls:
                    image_name = urlparse(image_url).path.split('/')[-1]
                    article_image_dir = os.path.join(article_dir, filename.replace('.json', ''))
                    Path(article_image_dir).mkdir(parents=True, exist_ok=True)  # Ensure the article-specific images directory exists
                    save_path = os.path.join(article_image_dir, image_name)
                    download_image(image_url, save_path)
                    print(f"Downloaded {image_name} to {save_path}")

if __name__ == '__main__':
    main()
