import sqlite3


class ApartmentDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
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

# Создаем базу данных и таблицу
db = ApartmentDatabase('apartment.db')
db.create_table()

# Вставляем тестовые данные
data = [
    ('Диван', 2020, 'Мебель', 'Гостиная'),
    ('Холодильник', 2018, 'Бытовая техника', 'Кухня'),
    ('Телевизор', 2021, 'Бытовая техника', 'Гостиная'),
    ('Кровать', 2019, 'Мебель', 'Спальная комната'),
]
db.insert_data(data)

# Закрываем соединение с базой данных
db.close()