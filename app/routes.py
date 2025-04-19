from fastapi import APIRouter, Depends, Query
from app.nyt_client import NYTClient
from app.schema import TopStoryArticle, ArticleSearchResult
from app.config import settings
from typing import List, Dict

router = APIRouter()

def get_nyt_client() -> NYTClient:
    return NYTClient(settings.nyt_api_key)

@router.get("/topstories", response_model=Dict[str, List[TopStoryArticle]])
async def get_top_stories(client: NYTClient = Depends(get_nyt_client)):
    sections = ["arts", "food", "movies", "travel", "science"]
    stories = {}
    for section in sections:
        articles = await client.fetch_top_stories(section)
        formatted = [
            TopStoryArticle(
                title=article["title"],
                section=article["section"],
                url=article["url"],
                abstract=article["abstract"],
                published_date=article["published_date"]
            )
            for article in articles
        ]
        stories[section] = formatted
    return stories

@router.get("/articlesearch", response_model=List[ArticleSearchResult])
async def search_articles(
    q: str = Query(..., description="Search keyword"),
    begin_date: str = Query(None, description="YYYYMMDD"),
    end_date: str = Query(None, description="YYYYMMDD"),
    client: NYTClient = Depends(get_nyt_client)
):
    raw_articles = await client.article_search(q, begin_date, end_date)
    return [
        ArticleSearchResult(
            headline=article["headline"]["main"],
            snippet=article["snippet"],
            web_url=article["web_url"],
            pub_date=article["pub_date"]
        )
        for article in raw_articles
    ]