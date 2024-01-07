# Student 클래스와 StudentManager 클래스를 작성합니다.
#모든 메소드를 채우세요

class Student:
    def __init__(self, name, student_id, score):


    def update_score(self, new_score):


    def __repr__(self):



class StudentManager:
    def __init__(self):


    def add_student(self, student):


    def remove_student(self, student_id):


    def get_students_with_score_above(self, threshold):


    def get_top_students(self, number_of_students):


    def __str__(self):




if __name__ == "__main__":
    # 학생 관리자 객체 생성 및 학생 목록 초기화
    manager = StudentManager()

    # 학생 추가
    manager.add_student(Student("홍길동", "2021001", 85))
    manager.add_student(Student("김철수", "2021002", 92))
    manager.add_student(Student("이영희", "2021003", 76))

    # 특정 점수 이상 학생 목록 조회
    students_above_80 = manager.get_students_with_score_above(80)
    print("점수가 80 이상인 학생들:")
    for student in students_above_80:
        print(student)

    # 상위 학생 목록 조회
    top_students = manager.get_top_students(2)
    print("\n상위 학생 목록:")
    for student in top_students:
        print(student)

    # 학생 관리자 상태 출력
    print("\n학생 관리자 상태:")
    print(manager)
