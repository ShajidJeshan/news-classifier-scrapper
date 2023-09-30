from fastapi import FastAPI
from .database import engine
from . import models
from .routers import history, scrape
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_pagination(app)

app.include_router(scrape.router)
app.include_router(history.router)