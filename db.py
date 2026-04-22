import mysql.connector
import os


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        database="atm",
        user="root",
        password=os.getenv("DB_PASSWORD")
    )