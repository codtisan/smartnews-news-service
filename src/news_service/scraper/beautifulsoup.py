from bs4 import BeautifulSoup
import asyncio
import requests

class BeautifulSoupScraper:

    async def scrape(self, url: str, selectors: list[str] = ['p']):
        response = requests.get(url)
        html = BeautifulSoup(response.content, 'html.parser')
        text_content = html.find_all(selectors)
        text = ''
        for content in text_content:
            text += content.text
        return text

    async def batch_scrape(self, urls: list[str], selectors: list[str] = ['p']):
        scraping_tasks = [self.scrape(url, selectors) for url in urls]
        results = await asyncio.gather(*scraping_tasks)
        return results