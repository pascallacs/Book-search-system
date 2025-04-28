import random
from typing import List, Dict

def generate_response(prompt: str, books: List[Dict]) -> str:
    keywords = set(prompt.lower().split())
    
    matched_books = []
    for book in books:
        book_keywords = set()
        book_keywords.update(book['title'].lower().split())
        book_keywords.update(book['author'].lower().split())
        book_keywords.add(book['genre'].lower())
        
        if keywords & book_keywords:
            matched_books.append(book)
    
    selected_book = random.choice(matched_books) if matched_books else random.choice(books)
    
    if matched_books:
        return f"Based on your interest in '{prompt}', I recommend reading '{selected_book['title']}' by {selected_book['author']}."
    else:
        return f"I'm not sure about books on '{prompt}', but you might enjoy '{selected_book['title']}' by {selected_book['author']}."