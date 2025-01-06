from flask import Flask, request, jsonify
from flask_cors import CORS 
from app.models import insert_book, get_books, get_book_by_version, update_book, delete_book

app = Flask(__name__)

CORS(app)

@app.route('/books', methods=['GET'])
def get_books_route():
    """Retrieves all books from the database."""
    books = get_books()
    
    # Convert the list of books to a list of dictionaries
    books_dict = [{
        '_version_': book[0],
        'title': book[1],
        'author_name': book[2],
        'first_publish_year': book[3],
        'publisher': book[4],
        'subject': book[5],
        'stock': book[6]
    } for book in books]
    
    return jsonify(books_dict)

@app.route('/books/<string:version>', methods=['GET'])
def get_book_route(version):
    """Retrieve a single book by its _version_."""
    book = get_book_by_version(version)  # Use the model function to get the book
    
    if book:
        # Convert the book to a dictionary and return it as JSON
        book_dict = {
            '_version_': book[0],
            'title': book[1],
            'author_name': book[2],
            'first_publish_year': book[3],
            'publisher': book[4],
            'subject': book[5],
            'stock': book[6]
        }
        return jsonify(book_dict)
    else:
        return jsonify({"error": "Book not found"}), 404


@app.route('/books', methods=['POST'])
def add_book_route():
    """Inserts a new book."""
    book = request.get_json()
    if '_version_' not in book:
        return jsonify({"error": "_version_ is required"}), 400  # Validation for _version_
    
    # Insert the book into the database
    insert_book(book)
    
    # Devuelve el libro insertado, puedes incluir más detalles si lo necesitas
    return jsonify(book), 201


@app.route('/books', methods=['PUT'])
def update_book_route():
    """Updates a book's data by its _version_."""
    book = request.get_json()
    version = book.get('_version_')  # Get _version_ from the object
    if not version:
        return jsonify({"error": "_version_ is required"}), 400  # Validation for _version_

    # Check if the book exists
    existing_book = get_book_by_version(version)  # Retrieve the book by its version
    if not existing_book:
        return jsonify({"error": "Book not found"}), 404  # If the book doesn't exist, return 404

    # Update all fields present in the request body
    updated_fields = {key: value for key, value in book.items() if key != '_version_'}
    
    update_book(version, updated_fields)

    # After update, get the updated book to return it
    updated_book = get_book_by_version(version)  # Retrieve the updated book

    # Make sure to return the updated book as an object, not as an array
    return jsonify(updated_book)  # Return the updated book as an object


@app.route('/books/<int:version>', methods=['DELETE'])
def delete_book_route(version):
    """Deletes a book by its _version_."""
    # Check if the book exists
    existing_book = get_book_by_version(version)  # Retrieve the book by its version
    if not existing_book:
        return jsonify({"error": "Book not found"}), 404  # If the book doesn't exist, return 404

    delete_book(version)
    return jsonify({"message": f"Book with version {version} deleted successfully!"})

