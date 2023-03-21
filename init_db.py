import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user (id, name, email, profile_pic) VALUES (?, ?, ?, ?)",
            ('1', 'Test', 'test@test.com', 'test.jpg')
            )

connection.commit()
connection.close()
