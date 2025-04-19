import httpx
from typing import List, Dict

class NYTClient:
    BASE_URL = "https://api.nytimes.com/"

    def __init__(self, api_key: str):
        self.api_key = api_key
    
    async def fetch_top_stories(self, section: str) -> List[Dict]:
        url = f"{self.BASE_URL}/svc/topstories/v2/{section}.json"
        params = {"api-key": self.api_key}
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json().get("results", [])[:2]

    async def article_search(self, section: str) -> List[Dict]:
        pass
