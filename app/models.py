# Aquí podemos definir funciones que interactúan directamente con la base de datos
from app.db import get_db_connection

def insert_book(book):
    """Inserta un libro en la base de datos"""
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
    """Obtiene todos los libros de la base de datos"""
    query = "SELECT * FROM books;"
    conn = get_db_connection()
    books = []
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        books = cursor.fetchall()  # Devuelve todas las filas
        cursor.close()
        conn.close()
    return books
