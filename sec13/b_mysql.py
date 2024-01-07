import mysql.connector
def my_conn():
      config = {
        'user': 'root',
        'password': '0000',
        'host': '127.0.0.1',
        'database': 'my_emp',
        'raise_on_warnings': True
      }
      cnx = mysql.connector.connect(**config)
      print(cnx)
      return cnx
def  select_All(conn):
    cur  = conn.cursor()
    cur.execute("select  * from emp")  #return 없이 실행 되는 구문
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    #연결 객체를 생선한 곳에서 소멸을 구현한다.
    select_All(my_conn())