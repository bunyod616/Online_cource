import psycopg2 as db
import os
from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    def connect(query, type):
        database = db.connect(
            database=os.getenv("name"),
            host=os.getenv("host"),
            user=os.getenv("user"),
            password=os.getenv("pasword"),
        )

        cursor = database.cursor()
        cursor.execute(query)
        query_data = ["insert", "create", 'update', "delete", "drop"]
        if type in query_data:
            database.commit()
            if type == "create":
                return "Created Successfull"

            elif type == "insert":
                return "Inserted"

            elif type == "delete":
                return "Deleted"

            elif type == "update":
                return "Updated"

        else:
            return cursor.fetchall()


