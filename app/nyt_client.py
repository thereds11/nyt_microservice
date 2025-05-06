import httpx
from fastapi import HTTPException
from typing import List, Dict

class NYTClient:
    BASE_URL = "https://api.nytimes.com/svc"

    def __init__(self, api_key: str):
        self.api_key = api_key
    
    async def fetch_top_stories(self, section: str) -> List[Dict]:
        url = f"{self.BASE_URL}/topstories/v2/{section}.json"
        params = {"api-key": self.api_key}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, params=params)
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail=f"NYT API Error: {e.response.text}")
            return response.json().get("results", [])[:2]

    async def article_search(self, q: str, begin_date: str = None, end_date: str = None) -> List[Dict]:
        url = f"{self.BASE_URL}/search/v2/articlesearch.json"
        params = {
            "api-key": self.api_key,
            "q": q
        }
        if begin_date:
            params["begin_date"] = begin_date
        if end_date:
            params["end_date"] = end_date
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, params=params)
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail=f"NYT API Error: {e.response.text}")
            return response.json().get("response", {}).get("docs", [])
