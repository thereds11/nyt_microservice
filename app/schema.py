from pydantic import BaseModel
from datetime import datetime

class TopStoryArticle(BaseModel):
    title: str
    section: str
    url: str
    abstract: str
    published_date: datetime

class ArticleSearchResult(BaseModel):
    headline: str
    snippet: str
    web_url: str
    pub_date: datetime