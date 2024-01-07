import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur = con.execute("CREATE TABLE lang(name, first_appeared)")  # first_appeared 칼럼 이름

data = (   {"name2": "C", "year": 1972},
           {"name2": "Fortran", "year": 1957},
           {"name2": "Python", "year": 1991},
           {"name2": "Go", "year": 2009},
        )
cur.executemany("INSERT INTO lang VALUES(:name2, :year)", data) # values값은 name, year

# params = (1972,)
params = (1957,)
cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params)
print(cur.fetchall())
con.close()
