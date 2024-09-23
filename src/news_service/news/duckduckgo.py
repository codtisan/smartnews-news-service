from duckduckgo_search import AsyncDDGS

class DuckduckgoNews:

    async def get_news(query: str, region: str = 'hk-tzh', duration: str = 'd', limit: int = 10):
        response = AsyncDDGS().news(keywords=query, region=region, timelimit=duration, max_results=limit)
        return response