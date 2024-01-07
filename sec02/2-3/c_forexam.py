def exam01():
    name = ['홍길동','박길동','최길동','김길동','이길동']
    age = [21,22,23,24,25]
    # 홍길동님의 나이는 00입니다. for , zip
    #print(list(zip(name,age)))
    for name, age in zip(name,age):
        print(f"{name}님의 나이는 {age} 입니다.")

#학생이름, 성적리스트, 주전공분야 -> key, value 로 만들기

def exam02(): # 다시 풀어보기
    name = ['홍길동','박길동','최길동','김길동','이길동']
    major = ["de", "da", "ds" ,"pm", "dc"]
    score = [91,82,23,24,25]

    students_info = [{'name':n, 'score': s, 'major':m} for n,s,m in zip(name,score,major)]
    for student in students_info:
        print(student)

def exam03():
    name = ['홍길동', '박길동', '최길동', '김길동', '이길동']
    age = [21, 22, 23, 24, 25]
    res=[f"{name}님의 나이는 {age} 입니다." for name, age in zip(name,age)]
    print(res)


def exam04():
    a = [f"{i} * {j} = {i * j} " for i in range(2,10,2) for j in range(2,9,2)]
    print(a)

if __name__ == "__main__":
    exam04()
