import sqlite3


conn = sqlite3.connect("test_database.db")
cur = conn.cursor()


def create():
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INT, title TEXT, year INT)")



def passive_insert():
    cur.execute("INSERT INTO books VALUES(1, 'Financier', 1991)")
    conn.commit()
    cur.close()
    conn.close()


def active_insert(id, title, year):
    cur.execute("INSERT INTO books VALUES(%d, '%s', %d)"%(id, title, year))
    conn.commit()
    cur.close()
    conn.close()
    
    


#for i in range(3,10):
#    active_insert(i, "Homo Deus", 1992)

def selector():
    cur.execute("SELECT * FROM books WHERE")
    for temp in cur.fetchall():
        print(temp)

selector()


a = 1
b = 10
c = 0


try:
    result = (a+b)/c
except :
    print("Something Wrong!")

    