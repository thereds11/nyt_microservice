from fastapi import APIRouter

router = APIRouter()

@router.get("/topstories")
async def get_top_stories():
    return {"message": "Top stories endpoint"}

@router.get("/articlesearch")
async def search_articles():
    return {"message": "Article search endpoint"}