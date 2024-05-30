import mysql.connector
from util.property_util import PropertyUtil
class DBConnection:
    connection = None
    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                # Get the connection string from PropertyUtil
                connection_string = PropertyUtil.get_property_string()

                # Split the connection string into components
                params = dict(item.split("=") for item in connection_string.split(" "))

                # Establish the connection using the extracted parameters
                DBConnection.connection = mysql.connector.connect(
                    host=params['host'],
                    database=params['dbname'],
                    user=params['user'],
                    password=params['password'],
                    port=int(params['port'])
                )
                print("Connection established successfully")
            except mysql.connector.Error as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        return DBConnection.connection
