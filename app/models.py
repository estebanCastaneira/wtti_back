from app.db import get_db_connection

def insert_book(book):
    """
    Inserts a book into the database.
    :param book: Dictionary containing the book details.
    """
    query = """
    INSERT INTO books (_version_, title, author_name, first_publish_year, publisher, subject, stock)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query, (book['_version_'], book['title'], book['author_name'], book['first_publish_year'], book['publisher'], book['subject'], book['stock']))
        conn.commit()
        cursor.close()
        conn.close()

def get_books():
    """
    Retrieves all books from the database.
    :return: List of all books in the database.
    """
    query = "SELECT * FROM books;"
    conn = get_db_connection()
    books = []
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        books = cursor.fetchall() 
        cursor.close()
        conn.close()
    return books

def get_book_by_version(version):
    """Retrieve a single book by its _version_."""
    query = "SELECT * FROM books WHERE _version_ = %s;"
    conn = get_db_connection()
    book = None
    if conn:
        cursor = conn.cursor()
        cursor.execute(query, (version,))
        book = cursor.fetchone()
        cursor.close()
        conn.close()
    
    return book

def update_book(version, updated_fields):
    """
    Updates the fields of a book in the database.
    :param version: Identifier of the book.
    :param updated_fields: Dictionary with the fields to update.
    """
    set_clause = ", ".join([f"{key} = %s" for key in updated_fields.keys()])
    query = f"UPDATE books SET {set_clause} WHERE _version_ = %s;"
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query, (*updated_fields.values(), version))
        conn.commit()
        cursor.close()
        conn.close()

def delete_book(version):
    """
    Deletes a book from the database by its identifier.
    :param version: Identifier of the book.
    """
    query = "DELETE FROM books WHERE _version_ = %s;"
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query, (version,))
        conn.commit()
        cursor.close()
        conn.close()
