import mysql.connector
from mysql.connector import Error

try:
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mxstream12'
    )

    if database.is_connected():
        cursorObject = database.cursor()
        cursorObject.execute("CREATE DATABASE elderco")
        print("All Done!")

except Error as e:
    print(f"Error: {e}")

finally:
    if (database.is_connected()):
        cursorObject.close()
        database.close()
        print("MySQL connection is closed")


