# NYTimes Article Microservice

A lightweight FastAPI-based microservice that integrates with the [New York Times Developer APIs](https://developer.nytimes.com/) to serve top news stories and article search results.

---

## Features

- REST API built with FastAPI
- Integration with:
    - [NYT Top Stories API](https://developer.nytimes.com/docs/top-stories-product/1/overview)
    - [NYT Article Search API](https://developer.nytimes.com/docs/articlesearch-product/1/overview)
- Typing and validation using Pydantic
- Async HTTP calls via `httpx`

---

## Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/thereds11/nyt_microservice.git
cd nyt_microservice
```

### 2. Create virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create `.env` file
```env
NYT_API_KEY=your_real_api_key
```

### 4. Run the App
```bash
uvicorn app.main:app --reload
```
Visit: http://localhost:8000/docs

---

## Run Tests

```bash
PYTHONPATH=. pytest
```

## API Endpoints

- `GET /nytimes/topstories`
Returns the 2 latest stories from each section: `arts`, `food`, `movies`, `travel`, `science`.

Response:
```json
{
  "arts": [
    {
      "title": "...",
      "section": "arts",
      "url": "...",
      "abstract": "...",
      "published_date": "2023-01-01T10:00:00"
    }
  ],
  ...
}
```

- `GET /nytimes/articlesearch`
Search NYTimes articles by keyword and optional date range.

Query Parameters:
    - `q`: search term (required)
    - `begin_date`: format `YYYYMMDD` (optional)
    - `end_date`: format `YYYYMMDD` (optional)

Response:
```json
[
  {
    "headline": "Article Title",
    "snippet": "Summary...",
    "web_url": "...",
    "pub_date": "2023-01-01T12:00:00"
  }
]
```