# Book-search-system
A FastAPI-powered REST API for searching and recommending books from an SQLite database.


**STEPS TO RUN**

Install dependencies:
-bash-
pip install -r requirements.txt


Initialize the database:
-bash-
sqlite3 data/books.db < data/schema.sql

Run the API:
-bash-
uvicorn app.main:app --reload

Access endpoints:
API Docs: http://localhost:8000/docs
All books: GET /books
