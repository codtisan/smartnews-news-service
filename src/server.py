from fastapi import FastAPI
from news_service.news.duckduckgo import DuckduckgoNews
from news_service.scraper.beautifulsoup import BeautifulSoupScraper
from news_service.llms.ollama import OllamaChat
import asyncio
from news_service.vectorstores.qdrant import Qdrant

app = FastAPI()

NEWS_CATEGORIES = ["政治", "經濟", "文化"]

@app.get("/")
async def check_health():
    return {
        'status': 'success',
        'status_code': 200,
        'message': 'OK!'
    }

@app.get("/news/collect")
async def collect_news():
    async def collect_news_by_topic(topic: str):
        news_data = await DuckduckgoNews.get_news(query=topic, limit=1)
        news_urls = [news['url'] for news in news_data]
        news_titles = [news['title'] for news in news_data]
        news_contents = await BeautifulSoupScraper().batch_scrape(urls=news_urls)
        embeddings = await OllamaChat().embed(news_titles)
        summaries = await OllamaChat().batch_summarize(new_contents=news_contents, news_titles=news_titles)
        payloads = []
        for index, news in enumerate(news_data): 
            payload = {
                **news,
                **{
                    "summary": summaries[index]
                }
            }
            payloads.append(payload)
        await Qdrant().batch_insert("news", embeddings, payloads)

    collecting_tasks = [collect_news_by_topic(category) for category in NEWS_CATEGORIES]
    await asyncio.gather(*collecting_tasks)

    return {
        'status': 'success',
        'status_code': 200,
        'message': 'OK!'
    }