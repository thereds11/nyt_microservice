from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI(
    title="NYTimes Article Microservice",
    description="Serves NYT Top Stories and Article Search Data",
    version="1.0.0"
)

app.include_router(api_router, prefix="/nytimes")