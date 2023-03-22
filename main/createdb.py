import sqlite3

conn = sqlite3.connect('pessoas.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        email TEXT
    )
''')

conn.commit()
