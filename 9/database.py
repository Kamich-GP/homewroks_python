import sqlite3

db = sqlite3.connect('mybot.db')

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT, phone_number TEXT)""")

def add_in_database(id, name, number):

    db = sqlite3.connect('mybot.db')
    c = db.cursor()

    c.execute("""INSERT INTO users VALUES (?, ?, ?)""", (id, name, number))
    db.commit()

    a = c.execute("""SELECT * FROM users""").fetchall()
    print(a)
# def add_id_in_date(id):
#
#     c.execute("""INSERT INTO users (id) VALUES (?)""", (id,))
#     db.commit()
#
# def add_name_in_date(name):
#
#     c.execute("""INSERT INTO users (name) VALUES (?)""", (name,))
#     db.commit()
#
# def add_numbre_in_date(phone_number):
#
#     c.execute("""INSERT INTO users (phone_number) VALUES (?)""", (phone_number,))
#     db.commit()
#
#     a = c.execute("""SELECT * FROM users""").fetchall()
#     print(a)
db.close()