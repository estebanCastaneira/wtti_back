from flask import Flask, request, jsonify
from app.models import insert_book, get_books

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books_route():
    books = get_books()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book_route():
    book = request.get_json()
    insert_book(book)
    return jsonify({"message": "Book added successfully!"}), 201
