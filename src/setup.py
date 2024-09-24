from news_service.vectorstores.qdrant import Qdrant
import asyncio

async def init_vectorstore():
    vectorstore = Qdrant()
    is_exist = await vectorstore.check_collection("news")
    if not is_exist:
        await vectorstore.create_collection("news", 2304)

def setup():
    asyncio.run(init_vectorstore())