import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

#cursor.execute('''
#    CREATE TABLE IF NOT EXISTS users (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        username TEXT NOT NULL,
#        password TEXT NOT NULL
#    )
#''')

#cursor.execute('''
#    INSERT INTO users (username, password) VALUES (?, ?)
#''', ('user1', 'password1'))

#users = [   
#    ('user9', 'password9'),
#    ('user10', 'password10'),
#     ('Галина', 'Карымова'), 
#]

#cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users)

#cursor.execute("SELECT * FROM users")
#users = cursor.fetchall()
#print(*users,sep='\n')

#cursor.execute("UPDATE users SET username='ИРИНА' WHERE id = 2")
cursor.execute("DELETE FROM users  WHERE id = 1")

conn.commit()
#print("Данные добавлены")
#print("Данные получены")

