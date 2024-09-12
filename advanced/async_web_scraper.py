# async_web_scraper.py
# Dependencies: aiohttp, beautifulsoup4
# Install with: pip install aiohttp beautifulsoup4

import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_website(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BeautifulSoup(html, 'html.parser')
        titles = [title.get_text() for title in soup.find_all('h1')]
        return titles

if __name__ == "__main__":
    url = input("Enter the URL of the website to scrape: ")
    titles = asyncio.run(scrape_website(url))
    print("Page Titles:")
    for title in titles:
        print(title)
