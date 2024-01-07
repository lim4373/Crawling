'''
name   kor  eng  mat => score
홍길동   90    80   70 => s1
정길동   50    60   70 => s2
이길동   100 100   100 => s3
'''

class Score:
    def __init__(self,name,kor,eng,mat): # 객체를 생성할 때 값을 받으면서 생성하겠다. (초기값을 자동으로 생성하지 않고 받아서 초기화 )
        self.name = name
        self.kor = kor
        self.eng= eng
        self.mat= mat


if __name__=="__main__":
    s1 = Score("홍길동", 90 ,  80,70)
    s2 = Score("정길동",   50,    60 ,  70)
    s3 = Score("이길동", 100, 100,   100)


    print(f"name = {s1.name} kor = {s1.kor} eng = {s1.eng} mat= {s1.mat}")
    print(f"name = {s2.name} kor = {s2.kor} eng = {s2.eng} mat= {s2.mat}")
    print(f"name = {s3.name} kor = {s3.kor} eng = {s3.eng} mat= {s3.mat}")