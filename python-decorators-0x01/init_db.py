import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', [
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com')
])
conn.commit()
conn.close()
print("users.db initialized.")
