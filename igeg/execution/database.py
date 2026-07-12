import sqlite3


class SQLiteDatabase:


    def __init__(self, db_path):

        self.connection = sqlite3.connect(
            db_path
        )


    def execute(self, query):

        cursor = self.connection.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        columns = [
            description[0]
            for description in cursor.description
        ]

        return columns, rows