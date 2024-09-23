from fastapi import FastAPI
from news_service.news.duckduckgo import DuckduckgoNews
from news_service.scraper.beautifulsoup import BeautifulSoupScraper
from news_service.llms.ollama import OllamaChat
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
    news_titles = [news['title'] for news in news_data]
    news_content = await BeautifulSoupScraper().batch_scrape(urls=news_urls)
    summary = await OllamaChat().summarize(news_content=news_content[0], news_title=news_data[0]['title'])
    print(summary)
    return {
        'status': 'success',
        'status_code': 200,
        'message': 'OK!'
    }