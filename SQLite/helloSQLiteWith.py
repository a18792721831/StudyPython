import sqlite3

linkUrl = 'hello.db'

with sqlite3.connect(linkUrl) as db :
    cur = db.cursor()
    print(dir(cur))
    sqlSelect = 'select * from user'
    delete_data = cur.execute(sqlSelect)
    print(delete_data.fetchall())