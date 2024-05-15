import sqlite3


class ApartmentDatabase:
    def __init__(self, db_name, path):
        self.conn = sqlite3.connect(path + "/" + db_name + '.db')
        self.cursor = self.conn.cursor()

    def create_table_items(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                year INTEGER NOT NULL,
                type TEXT NOT NULL,
                room TEXT NOT NULL
            )
        """)

    def insert_data(self, data):
        self.cursor.executemany("""
            INSERT INTO items (name, year, type, room) VALUES (?, ?, ?, ?)
        """, data)
        self.conn.commit()

    def close(self):
        self.conn.close()
