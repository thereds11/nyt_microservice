import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from typing import List
from app.main import app

fake_top_stories = [
    {
        "title": "Sample Title 1",
        "section": "arts",
        "url": "https://example.com/article1",
        "abstract": "Sample abstract 1",
        "published_date": "2023-01-01T10:00:00Z"
    },
    {
        "title": "Sample Title 2",
        "section": "arts",
        "url": "https://example.com/article2",
        "abstract": "Sample abstract 2",
        "published_date": "2023-01-02T11:00:00Z"
    },
]

fake_articles = [
    {
        "headline": { "main": "Fake News Article" },
        "snippet": "This is a test snippet.",
        "web_url": "https://example.com/fake-article",
        "pub_date": "2023-01-01T12:00:00Z"
    },
    {
        "headline": { "main": "Another Fake Article" },
        "snippet": "Second snippet here.",
        "web_url": "https://example.com/another-fake",
        "pub_date": "2023-01-02T14:00:00Z"
    }
]

class MockTopStoriesClient:
    async def fetch_top_stories(self, section: str) -> List[dict]:
        return fake_top_stories
    async def article_search(self, q: str, begin_date: str = None, end_date: str = None) -> List[dict]:
        return fake_articles

from app.routes import get_nyt_client
app.dependency_overrides[get_nyt_client] = lambda: MockTopStoriesClient()

@pytest.mark.asyncio
async def test_topstories_return_expected_structure():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/nytimes/topstories")
        assert response.status_code == 200
        data = response.json()

        for section in ["arts"]:
            assert isinstance(data[section], list)
            assert len(data[section]) == 2

@pytest.mark.asyncio
async def test_articlesearch_returns_expected_data():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/nytimes/articlesearch?q=test")
        assert response.status_code == 200
        data = response.json()
        assert data[0]["headline"] == "Fake News Article"