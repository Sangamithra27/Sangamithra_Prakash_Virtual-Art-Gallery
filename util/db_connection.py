import mysql.connector

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                DBConnection.connection = mysql.connector.connect(
                    host='localhost',
                    database='virtualartgallery',
                    user='root',
                    password='SYSTEM',
                    port=3306
                )
                print("Connection established successfully")
            except Exception as e:
                print(f"Error: {e}")
        return DBConnection.connection