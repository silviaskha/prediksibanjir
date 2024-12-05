
import mysql.connector
from mysql.connector import Error
try:
    db_connection = mysql.connector.connect(
        host="localhost",
        port=3306,  # Port MySQL yang baru
        user="root",
        password="",  # Ganti dengan password MySQL Anda
        database="floodcast"
    )
    if db_connection.is_connected():
        print("Connected to MySQL database")
except Error as e:
    print(f"Error: {e}")
finally:
    if db_connection.is_connected():
        db_connection.close()
        print("Connection closed")
