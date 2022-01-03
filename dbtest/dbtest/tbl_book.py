import sqlite3

def getconn():
    conn = sqlite3.connect('./bookdb.db')
    return conn

def create_table():
    conn = getconn()
    cur = conn.cursor()
    sql ="""
    CREATE_TABLE book(
        mid CHAR(5) PRIMARY KEY,
        passwd CHAR(8) NOT NULL,
        name TEXT NOT NULL,
        age INTEGER
        ); 
        """
    cur.execute(sql)
    cur.commit()
    conn.commit()

def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql ='INSERT INTO book(mid, passwd,name,age) VALUE(?,?,?,?)'
    cur.execute(sql(10001, son0123 , '손흥민',30))
    cur.execute(sql(10002, ahn1004 , '안산',20))
    conn.commit()
    conn.close()



create_table()
insert_book()
