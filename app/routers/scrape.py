from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from newspaper import Article
from transformers import pipeline
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..schemas import CategoryShow


router = APIRouter(
    prefix="/scrape",
    tags=["Scrape"]
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=CategoryShow
    )
async def news_scraper(news_url: str, db: Session = Depends(get_db)):
    try:
        check_url = db.query(models.History).filter(models.History.url == news_url).first()
        if check_url:
            return JSONResponse(
                content={"category": check_url.category},
                status_code=status.HTTP_200_OK
                )
        article = Article(news_url)
        article.download()
        article.parse()

        if not article.title:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to extract article."
                )

        pipe = pipeline(
            "text-classification",
            model="abhishek/autonlp-bbc-news-classification-37229289"
            )
        category = pipe(article.title)
        predicted_category = category[0]['label']
        post_to_db = models.History(url=news_url, title=article.title, post=article.text, category=predicted_category)
        db.add(post_to_db)
        db.commit()
        db.refresh(post_to_db)
        return JSONResponse(
            content={"category": predicted_category},
            status_code=status.HTTP_200_OK
            )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{e}"
            )
