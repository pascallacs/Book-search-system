from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import Book, QueryRequest
from .database import get_db, get_books, get_books_by_genre, count_books_by_author, get_books_after_year
from .prompts import generate_response
from typing import List
from .models import Book
import sqlite3

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Book Search System",
        "endpoints": {
            "all_books": "/books",
            "book_recommendation": "/query (POST)",
            "books_by_genre": "/books/genre/{genre}",
            "count_by_author": "/books/count/{author}",
            "recent_books": "/books/recent/{year}"
        }
    }
    
@app.on_event("startup")
async def startup():
    app.db_conn = get_db()

@app.on_event("shutdown")
async def shutdown():
    app.db_conn.close()

@app.get("/books", response_model=List[Book])
async def list_books():
    try:
        books = get_books(app.db_conn)
        return books
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
async def handle_query(query: QueryRequest):
    try:
        books = get_books(app.db_conn)
        response = generate_response(query.prompt, books)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/books/genre/{genre}")
async def books_by_genre(genre: str):
    try:
        books = get_books_by_genre(app.db_conn, genre)
        return books
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/books/count/{author}")
async def count_books(author: str):
    try:
        count = count_books_by_author(app.db_conn, author)
        return {"author": author, "count": count}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/books/recent/{year}")
async def recent_books(year: int = 2015):
    try:
        books = get_books_after_year(app.db_conn, year)
        return books
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
