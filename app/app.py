from app.routes import app
from app.db import create_books_table

if __name__ == "__main__":
    create_books_table()
    app.run(debug=True)

