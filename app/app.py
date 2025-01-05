from app.db import get_db_connection

def test_db_connection():
    conn = get_db_connection()
    if conn:
        print("Conexión exitosa a la base de datos")
        conn.close()
    else:
        print("Error al conectar con la base de datos")

if __name__ == "__main__":
    test_db_connection()
