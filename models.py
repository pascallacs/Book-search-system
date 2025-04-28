from pydantic import BaseModel
from typing import List


class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    year: int

    class Config:
        from_attributes = True

class QueryRequest(BaseModel):
    prompt: str