import sqlite3
con=sqlite3.connect("first.db")  # insert, delete, update  -> commit(), rollback()
print(type(con))
cur = con.cursor()  # 명령을 실행하겟다.
cur.execute("CREATE TABLE movie(title, year, score)")
insert_sql  =  "insert into movie values(1,1,1)"
cur.execute(insert_sql)
con.commit()
res = cur.execute("SELECT * FROM movie")
print(res.fetchone())
con.close()