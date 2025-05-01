

from fastapi import FastAPI
import uvicorn
from app.api.routes import router

app = FastAPI(
    title="Financial Data Aggregator",
    version="1.0.0"
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
