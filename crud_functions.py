import sqlite3

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Создаем таблицу Products, если она еще не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            photo_url TEXT NOT NULL
        )
    ''')

    # Создаем таблицу Users, если она еще не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (username, email, age, 1000))
    conn.commit()
    conn.close()

def is_included(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Users WHERE username = ?", (username,))
    count = cursor.fetchone()[0]
    conn.close()

    return count > 0


# Получение всех записей из таблицы Products
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    product_list = []
    for product in products:
        id, title, description, price, photo_url = product
        product_list.append((id, title, description, price, [photo_url]))

    conn.close()
    return product_list


def insert_sample_data():
    sample_products = [
        ("Product1", "описание 1", 100, "https://medicrashodka.ru/image/cache/data/upakovi/mp3162/banka-dlya-proteina-1-500x500.jpg"),
        ("Product2", "описание 2", 200, "https://yarus-market.ru/image/cache/data-tara-dlya-kosmetiki-i-mediciny-banki-dlya-bad-dlya-upakovki-drazhe-kapsul-vitaminov-09-kruglaya-banka-dlya-sportivnogo-pitaniya-5-600x600.jpg"),
        ("Product3", "описание 3", 300, "https://yarus-market.ru/image/cache/data-tara-dlya-kosmetiki-i-mediciny-banki-dlya-bad-dlya-upakovki-drazhe-kapsul-vitaminov-06-uzkaya-banka-pet-s-vintovoj-kryshkoj-bad-cilinrt-01-600x600.jpg"),
        ("Product4", "описание 4", 400, "https://yarus-market.ru/image/cache/data-tara-dlya-kosmetiki-i-mediciny-banki-dlya-bad-dlya-upakovki-drazhe-kapsul-vitaminov-07-shirokaya-cilindricheskaya-banka-pet-bad-cilind-big-01-600x600.jpg")
    ]

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO Products (title, description, price, photo_url) VALUES (?, ?, ?, ?)", sample_products)

    conn.commit()
    conn.close()


# Вызов функции для создания базы данных и заполнения её данными
if __name__ == "__main__":
    initiate_db()
    insert_sample_data()