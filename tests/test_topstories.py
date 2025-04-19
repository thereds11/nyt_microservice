import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from typing import List
from app.main import app
from app.nyt_client import NYTClient

fake_articles = [
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

class MockNYTClient:
    async def fetch_top_stories(self, section: str) -> List[dict]:
        return fake_articles

app.dependency_overrides[NYTClient] = lambda: MockNYTClient()

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