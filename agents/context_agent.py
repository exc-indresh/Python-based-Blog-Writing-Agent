import aiohttp
from core.config import NEWSDATA_API_KEY
from functools import lru_cache

async def fetch_news_data(topic):
    url = f"https://newsdata.io/api/1/news?apikey={NEWSDATA_API_KEY}&q={topic}&language=en"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()

@lru_cache(maxsize=128)
async def fetch_datamuse_keywords(topic):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.datamuse.com/words?ml={topic}") as resp:
            try:
                return await resp.json()
            except aiohttp.ContentTypeError:
                print(f"[bold red]❌ Datamuse API returned unexpected content. Skipping keywords.")
                return []


