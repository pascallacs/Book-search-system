import sqlite3
from typing import List, Dict, Any

def get_db():
    conn = sqlite3.connect('data/books.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_books(conn) -> List[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    return [dict(row) for row in cursor.fetchall()]

def get_books_by_genre(conn, genre: str) -> List[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE genre = ?", (genre,))
    return [dict(row) for row in cursor.fetchall()]

def count_books_by_author(conn, author: str) -> int:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM books WHERE author = ?", (author,))
    return cursor.fetchone()[0]

def get_books_after_year(conn, year: int) -> List[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE year > ?", (year,))
    return [dict(row) for row in cursor.fetchall()]