import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    connection.commit()
    return cursor.fetchall()


initiate_db()

# for i in range(1, 5):
#     cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
#                    (f'Продукт {i}', f'Описание {i}', str(i * 100)))
