# web_scraper.py
# Dependencies: requests, beautifulsoup4
# Install with: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = [h.text for h in soup.find_all('h2')]
    return headlines

def save_to_csv(data, filename):
    df = pd.DataFrame(data, columns=['Headlines'])
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    url = 'https://news.ycombinator.com/'
    headlines = scrape_website(url)
    save_to_csv(headlines, 'headlines.csv')
    print("Headlines saved to headlines.csv")
