'''  json 타입의 문자열을   파이썬 모듈로  인코딩, 디코딩   -> mysql  '''
import mysql.connector   # 테이블 생성, insert, select
import json

def db_connect(): # db연결
    config = {
        'user': 'root',
        'password': '0000',
        'host': '127.0.0.1',
        'database': 'my_emp'
    }
    return  mysql.connector.connect(**config)

def  create_table():
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students_123 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data JSON NOT NULL
        )
    """)
    cursor.close()
    cnx.close()

def insert():
    ########2. 입력할 데이터를  {} 선언하고 insert
    cnx = db_connect()
    cursor = cnx.cursor()
    data = {
        "STUDENT": [
            {"NAME": "Dominica", "SCORE": {"KOR": 10, "ENG": 20, "MATH": 30}},
            {"NAME": "Dominico", "SCORE": {"KOR": 90, "ENG": 40, "MATH": 100}},
            {"NAME": "RuRe", "SCORE": {"KOR": 90, "ENG": 90, "MATH": 90}}
        ]
    }

    cursor.execute("INSERT INTO students (data) VALUES (%s)", (json.dumps(data),))
    cnx.commit()
    cursor.close()
    cnx.close()

#### 3. 테이블 생성 및 데이터를 mysql에서 확인
def select():
    ##### 4.전체 출력 및 json_type json.loads(row[0]) 로 결과를 추출
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT data FROM students")
    rows = cursor.fetchall()
    for row in rows:
        #print(json.loads(row[0]))  #전체 출력
        json_data =json.loads(row[0]) #이름만 출력
        print(type(json_data))
        students  =json_data.get("STUDENT",[])
        for  student in students:
            name = student.get("NAME")
            print(name)
    cursor.close()
    cnx.close()

def select_name():
    ####5. mysql query로 name을 추출하고 싶다.
    cnx = db_connect()
    cursor = cnx.cursor()
    query  = "SELECT  data -> '$.STUDENT[*].NAME'    FROM   students"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        names  = row[0]
        print(names)
    cursor.close()
    cnx.close()

###6. 점수의 합을 구하고 싶다.
def select_sum_scores():
    cnx = db_connect()
    cursor = cnx.cursor()
    query  = "SELECT  data -> '$.STUDENT[*].SCORE'    FROM   students"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        scores_json = row[0]
        scores_list = json.loads(scores_json)  #[]로 리턴한다
        for scores_dict in scores_list:
            sum_score = sum(scores_dict.values())
            print(f"Sum of scores: {sum_score}")

    cursor.close()
    cnx.close()
## 영상보고 따라하기
if __name__ == '__main__':
    create_table()
    insert()

# https://dev.mysql.com/doc/refman/8.0/en/json.html#json-values
# https://dev.mysql.com/doc/refman/8.0/en/json-table-functions.html
# https://jsonlines.org/