from pydantic import BaseModel
from datetime import datetime

class TopStoryArticle(BaseModel):
    title: str
    section: str
    url: str
    abstract: str
    published_date: datetime