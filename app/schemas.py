from pydantic import BaseModel


class HistoryShow(BaseModel):
    url: str
    category: str

    class Config:
        from_attributes = True


class CategoryShow(BaseModel):
    category: str

    class Config:
        from_attributes = True
