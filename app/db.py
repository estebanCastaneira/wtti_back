import psycopg2
from app.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

def get_db_connection():
    """
    Establishes a connection to the PostgreSQL database using credentials from config.py.
    Returns the connection object if successful, otherwise returns None.
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_books_table():
    """
    Creates the 'books' table if it doesn't already exist.
    This function should be called at the start of the app to ensure the table is available.
    """
    query = """
    CREATE TABLE IF NOT EXISTS books (
        _version_ BIGINT PRIMARY KEY,
        title VARCHAR NOT NULL,
        author_name VARCHAR NOT NULL,
        first_publish_year INTEGER,
        publisher VARCHAR,
        subject VARCHAR,
        stock INTEGER
    );
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()
            print("Books table created (if not already exists).")
        except Exception as e:
            print(f"Error creating table: {e}")
            conn.rollback()
            conn.close()
    else:
        print("Failed to connect to the database while creating the table.")
