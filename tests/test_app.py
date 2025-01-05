import unittest
from app.models import insert_book, get_books
from app.db import get_db_connection

class TestApp(unittest.TestCase):

    def setUp(self):
        """Configura el entorno antes de cada prueba"""
        self.conn = get_db_connection()
        if self.conn:
            print("Conexión a la base de datos establecida correctamente")
        else:
            self.fail("No se pudo conectar a la base de datos")

    def test_insert_book(self):
        """Prueba la inserción de un libro en la base de datos"""
        book = {
            '_version_': '8.0',
            'title': 'Test Book',
            'author_name': 'Test Author',
            'first_publish_year': 2020,
            'publisher': 'Test Publisher',
            'subject': 'Test Subject',
            'stock': 10
        }
        
        insert_book(book)
        
        # Verificamos que el libro se haya insertado correctamente
        books = get_books()
        inserted_book = next((b for b in books if b[1] == 'Test Book'), None)
        
        self.assertIsNotNone(inserted_book, "El libro no fue insertado correctamente")
        self.assertEqual(inserted_book[1], 'Test Book', "El título del libro no coincide")

    def test_get_books(self):
        """Prueba la obtención de todos los libros desde la base de datos"""
        books = get_books()
        print(books)
        self.assertIsInstance(books, list, "La respuesta no es una lista de libros")
        self.assertGreater(len(books), 0, "No se encontraron libros en la base de datos")

    def tearDown(self):
        """Limpia después de cada prueba"""
        if self.conn:
            # Elimina el libro insertado en cada prueba
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM books WHERE _version_ = %s;", ('8.0',))  # Borra el libro por versión
            self.conn.commit()  # Confirma la eliminación
            cursor.close()
            self.conn.close()

if __name__ == "__main__":
    unittest.main()
