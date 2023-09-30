from fastapi import FastAPI
from .database import engine
from . import models
from .routers import history, scrape
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv('ALLOWED_ORIGIN'),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_pagination(app)

app.include_router(scrape.router)
app.include_router(history.router)

if __name__ == '__main__':
    uvicorn.run('app.main:app', reload=True)
