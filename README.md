# Getch Articles from Intercom Account

## Overview
This tool is designed for extracting articles from an Intercom account. It allows users to fetch article IDs, retrieve the articles along with their images, and generate Word documents with the content, ensuring grammar checks through OpenAI.

## Prerequisites
- Git
- Python 3.x
- Access to an Intercom account with API keys

## Installation and Setup

### Clone the Repository
Clone the repository from GitHub to your local machine:
```bash
git clone https://github.com/lvalics/intercom-fetch-articles/

## Install Dependencies
Navigate to the cloned directory and install the required Python packages:

```bash
cd intercom-fetch-articles
pip install -r requirements.txt

## Configure Environment Variables
Copy the .env.example file to a new file named .env.
Edit the .env file to include your Intercom API keys and other necessary configuration details.

### Usage
## Step 1: Get All Article IDs
Fetch all article IDs from your Intercom account. The IDs will be saved to a file.

```bash
python get_articles.py

## Step 2: Fetch Articles
Retrieve all articles from Intercom using the fetched IDs. Articles will be saved in a JSON file.

```bash
python fetch_article_data.py

## Step 3: Download Images
Process JSON files to extract image URLs and download them into a designated folder.

```bash
python fetch_images.py

## Step 4: Generate DOCX Files with Grammar Check
Generate DOCX files from the fetched articles.
Text is sent to OpenAI for grammar checks before finalizing the document.

```bash
python get_articles.py

## Notes
Ensure you have the necessary permissions on Intercom to access and extract article data.
Keep your API keys and sensitive information secure.
