import sqlite3


conn = sqlite3.connect("test_base.db")
cur = conn.cursor()

def create():
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INT, title TEXT, year INT)")

def passive_insert():
    cur.execute("INSERT INTO books VALUES(1, 'Financier', 1992)")
    conn.commit()
    cur.close()
    conn.close()

def active_insert(id, title, year):
    cur.execute("INSERT INTO books VALUES(%d, '%s',%d)"%(id, title, year))
    conn.commit()
    


def selector():
    cur.execute("SELECT * FROM books WHERE id > 50")
    for  i in cur.fetchall():
        print(i)

selector()
