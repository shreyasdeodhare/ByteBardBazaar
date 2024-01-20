import mysql.connector
from com.project.common.constants import *
class ApplicationConnection:
    _instance = None

    def __new__(cls):
        print("Creating new instance of DatabaseConnector")
        if not cls._instance:
            print("Initializing new instance")
            cls._instance = super(ApplicationConnection, cls).__new__(cls)
            cls._instance.mydb = cls._instance.connect_to_database()
            cls._instance.mycursor = cls._instance.mydb.cursor()
        return cls._instance

    def connect_to_database(self):
        # Add your database connection details here
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

    def disconnect_from_database(self):
        if hasattr(self._instance, 'mydb') and self._instance.mydb.is_connected():
            self._instance.mydb.close()
            print("Disconnected from the database.")
