from bs4 import BeautifulSoup
import asyncio
import requests
from news_service.scraper.config import AntiBlockSetting

class BeautifulSoupScraper:
    def __init__(self) -> None:
        self.headers = requests.utils.default_headers()
        self.headers.update({
            'User-Agent': AntiBlockSetting.USER_AGENT.value[0],
        })

    async def scrape(self, url: str, selectors: list[str] = ['p']):
        response = requests.get(url, headers=self.headers)
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