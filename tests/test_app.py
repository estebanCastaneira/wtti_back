import unittest
from app.models import insert_book, get_books, update_book, delete_book
from app.db import get_db_connection

class TestApp(unittest.TestCase):

    def setUp(self):
        """Sets up the environment before each test."""
        self.conn = get_db_connection()
        if self.conn:
            self.conn.autocommit = False  # Disable auto-commit to wrap tests in transactions
            cursor = self.conn.cursor()
            # Clean up any pre-existing test data
            cursor.execute("DELETE FROM books WHERE _version_ IN (%s, %s, %s, %s, %s);", (1, 2, 3, 4, 5))
            self.conn.commit()
            cursor.close()
        else:
            self.fail("Failed to connect to the database.")

    def test_insert_book(self):
        """Tests inserting a book into the database."""
        book = {
            '_version_': 1,
            'title': 'Test Book',
            'author_name': 'Test Author',
            'first_publish_year': 2020,
            'publisher': 'Test Publisher',
            'subject': 'Test Subject',
            'stock': 10
        }

        insert_book(book)

        # Verify the book was inserted correctly
        books = get_books()
        inserted_book = next((b for b in books if b[1] == 'Test Book'), None)

        self.assertIsNotNone(inserted_book, "The book was not inserted correctly.")
        self.assertEqual(inserted_book[1], 'Test Book', "The book title does not match.")

    def test_get_books(self):
        """Tests retrieving all books from the database."""
        # Insert a book to ensure the database is not empty
        book = {
            '_version_': 2,
            'title': 'Another Test Book',
            'author_name': 'Another Test Author',
            'first_publish_year': 2021,
            'publisher': 'Another Test Publisher',
            'subject': 'Another Test Subject',
            'stock': 5
        }
        insert_book(book)

        # Fetch all books
        books = get_books()
        self.assertIsInstance(books, list, "The response is not a list of books.")
        self.assertGreater(len(books), 0, "No books were found in the database.")

    def test_update_book(self):
        """Tests updating a book in the database."""
        # Insert a book to update
        book = {
            '_version_': 3,
            'title': 'Book to Update',
            'author_name': 'Author to Update',
            'first_publish_year': 2019,
            'publisher': 'Publisher to Update',
            'subject': 'Subject to Update',
            'stock': 7
        }
        insert_book(book)

        # Update the book
        updated_fields = {'title': 'Updated Book Title', 'stock': 15}
        update_book(3, updated_fields)

        # Verify the update
        books = get_books()
        updated_book = next((b for b in books if b[0] == 3), None)
        self.assertIsNotNone(updated_book, "The book to update was not found.")
        self.assertEqual(updated_book[1], 'Updated Book Title', "The book title was not updated correctly.")
        self.assertEqual(updated_book[6], 15, "The stock was not updated correctly.")

    def test_delete_book(self):
        """Tests deleting a book from the database."""
        # Insert a book to delete
        book = {
            '_version_': 5,
            'title': 'Book to Delete',
            'author_name': 'Author to Delete',
            'first_publish_year': 2018,
            'publisher': 'Publisher to Delete',
            'subject': 'Subject to Delete',
            'stock': 12
        }
        insert_book(book)

        # Delete the book
        delete_book(5)

        # Verify the deletion
        books = get_books()
        deleted_book = next((b for b in books if b[0] == 5), None)
        self.assertIsNone(deleted_book, "The book was not deleted correctly.")

    def tearDown(self):
        """Rolls back any changes after each test."""
        if self.conn:
            self.conn.rollback()  # Roll back the transaction
            self.conn.close()

if __name__ == "__main__":
    unittest.main()
