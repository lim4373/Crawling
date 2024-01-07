import mysql.connector
from dataclasses import dataclass

@dataclass
class Employee:
    id: int
    name: str
    age: int
    city: str

class EmployeeDB:
    def __init__(self, user, password, database):
        self.conn = mysql.connector.connect(
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS employees")
        self.cursor.execute('''
            CREATE TABLE employees (
                id    INTEGER AUTO_INCREMENT PRIMARY KEY, 
                name  VARCHAR(100) NOT NULL,       
                age   INTEGER NOT NULL, 
                city  VARCHAR(100) NOT NULL
            )
        ''')

    def insert_employees(self, employee: Employee):
        self.cursor.execute(
            'INSERT INTO employees (name, age, city) VALUES (%s, %s, %s)',
            (employee.name, employee.age, employee.city)
        )
        self.conn.commit()

    def selectall_employees(self):
        self.cursor.execute('SELECT * FROM employees')
        rows = self.cursor.fetchall()
        return [Employee(*row) for row in rows]

    def update_employees(self, employee: Employee):
        self.cursor.execute(
            'UPDATE employees SET name=%s, age=%s, city=%s WHERE id=%s',
            (employee.name, employee.age, employee.city, employee.id)
        )
        self.conn.commit()

    def delete_employees(self, id):
        self.cursor.execute('DELETE FROM employees WHERE id=%s', (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
    db = EmployeeDB("root", "0000", "my_emp")
    db.insert_employees(Employee(None, '홍길동1', 21, '서울1'))
    db.insert_employees(Employee(None, '홍길동2', 22, '서울2'))
    db.insert_employees(Employee(None, '홍길동3', 23, '서울3'))
    print("After insert:")
    print(db.selectall_employees())

    print("After Update:")
    db.update_employees(Employee(1, '정길동', 35, '인천'))
    print(db.selectall_employees())

    print("After delete:")
    # db.delete_employees(2)
    # print(db.selectall_employees())
