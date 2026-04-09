# Web Scraping Example 8
# This program demonstrates a basic web scraping using requests (without BeautifulSoup for simplicity).
# Note: For real-world scraping, consider using BeautifulSoup for parsing HTML.

import requests

url = "https://www.example.com"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully fetched content from {url}")
        # print(response.text[:500]) # Print first 500 characters of the content
    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
