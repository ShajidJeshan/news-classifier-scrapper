from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from sqlalchemy import desc
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from ..schemas import HistoryShow


router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=Page[HistoryShow]
    )
def get_history(db: Session = Depends(get_db), params: Params = Depends()):
    history = db.query(models.History).order_by(desc(models.History.created_at))
    if not history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="History not found"
            )
    return paginate(history, params)
