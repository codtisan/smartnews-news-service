from fastapi import FastAPI
from news_service.news.duckduckgo import DuckduckgoNews
from news_service.scraper.beautifulsoup import BeautifulSoupScraper

app = FastAPI()


@app.get("/")
async def check_health():
    return {
        'status': 'success',
        'status_code': 200,
        'message': 'OK!'
    }

@app.get("/news/collect")
async def collect_news():
    news_data = await DuckduckgoNews.get_news(query='經濟', limit=2)
    news_urls = [news['url'] for news in news_data]
    news_content = await BeautifulSoupScraper().batch_scrape(urls=news_urls)
    print(news_content)
    return {
        'status': 'success',
        'status_code': 200,
        'message': 'OK!'
    }