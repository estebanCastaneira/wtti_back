## Book Inventory Manager - Backend

### Overview

This repository contains the backend for the "Book Inventory Manager" application. It is designed to manage bookstore inventories efficiently by providing endpoints to perform CRUD operations on the database. The backend is built with **Python** using **Flask**, interacting with a PostgreSQL database through raw SQL and stored procedures.

### Features

- **Retrieve Books**: Fetch all books or a specific book by its version.
- **Add Books**: Insert new books into the inventory.
- **Update Books**: Modify existing book details based on their version.
- **Delete Books**: Remove books from the inventory.
- **Error Handling**: Robust error responses for invalid or missing data.

### Requirements

- **Python**: 3.12.3
- **PostgreSQL**: 14 or higher
- **Dependencies**:
  - blinker==1.9.0
  - click==8.1.8
  - Flask==3.1.0
  - Flask-Cors==5.0.0
  - iniconfig==2.0.0
  - itsdangerous==2.2.0
  - Jinja2==3.1.5
  - MarkupSafe==3.0.2
  - packaging==24.2
  - pluggy==1.5.0
  - psycopg2==2.9.10
  - pytest==8.3.4
  - python-dotenv==1.0.1
  - Werkzeug==3.1.3

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/estebanCastaneira/wtti_back
   cd wtti_back
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:

   Create a `.env` file based on `.env.example` and fill in your database credentials:

   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=book_inventory
   DB_USER=<your_username>
   DB_PASSWORD=<your_password>
   ```

### Project Structure

```plaintext
.
├── app/                   # Application code
│   ├── __init__.py        # Application factory
│   ├── app.py             # Main application entry point
│   ├── config.py          # Configuration settings
│   ├── db.py              # Database connection
│   ├── models.py          # Database operations
│   ├── routes.py          # API routes
├── tests/                 # Unit tests
│   ├── __init__.py
│   ├── test_app.py        # Test cases
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
└── README.md              # Documentation
```

### API Endpoints

#### `GET /books`

Fetch all books in the inventory.

- **Response**:
  ```json
  [
    {
      "_version_": 1,
      "title": "Book Title",
      "author_name": "Author Name",
      "first_publish_year": 2020,
      "publisher": "Publisher Name",
      "subject": "Subject",
      "stock": 10
    }
  ]
  ```

#### `GET /books/<string:version>`

Fetch a specific book by its version.

- **Response**:
  ```json
  {
    "_version_": 1,
    "title": "Book Title",
    "author_name": "Author Name",
    "first_publish_year": 2020,
    "publisher": "Publisher Name",
    "subject": "Subject",
    "stock": 10
  }
  ```

#### `POST /books`

Add a new book to the inventory.

- **Request Body**:

  ```json
  {
    "_version_": 1,
    "title": "Book Title",
    "author_name": "Author Name",
    "first_publish_year": 2020,
    "publisher": "Publisher Name",
    "subject": "Subject",
    "stock": 10
  }
  ```

- **Response**:
  ```json
  {
    "message": "Book added successfully."
  }
  ```

#### `PUT /books`

Update an existing book's details.

- **Request Body**:

  ```json
  {
    "_version_": 1,
    "title": "Updated Title",
    "stock": 15
  }
  ```

- **Response**:
  ```json
  {
    "message": "Book updated successfully."
  }
  ```

#### `DELETE /books/<int:version>`

Delete a book by its version.

- **Response**:
  ```json
  {
    "message": "Book with version 1 deleted successfully!"
  }
  ```

### Testing

1. Run unit tests:

   pytest tests/

2. Tests include:
   - **Insert Books**: Verifies books can be added.
   - **Retrieve Books**: Ensures books can be fetched.
   - **Update Books**: Validates books can be updated.
   - **Delete Books**: Checks books can be deleted.

### Security

Sensitive information like database credentials is managed through environment variables. The `.env.example` file serves as a template.
