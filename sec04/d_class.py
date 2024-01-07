'''
name   kor  eng  mat => score
홍길동   90    80   70 => s1
정길동   50    60   70 => s2
이길동   100 100   100 => s3
'''
'''
name   kor  eng  mat => score
홍길동   90    80   70 => s1
정길동   50    60   70 => s2
이길동   100 100   100 => s3
noname   0    0     0  => s4
박길동    0    0     0
'''
# 클래스를 선언하게 되면 모든 클래스의 수퍼인 object의 자식이 돼서 기능 및 변수등을 상속받게 된다,
class Score:
    def __init__(self,name="noname",kor=0,eng=0,mat=0)-> None :
        self.name = name
        self.kor = kor
        self.eng= eng
        self.mat= mat

    def __repr__(self)-> str : # 객체 변수를 호출할 때 자동으로 호출된다., return 해주는 str 이 있고
        return f"name = {self.name} kor = {self.kor} eng = {self.eng} mat= {self.mat}"
# repr 없으면 주소 나옴
if __name__=="__main__":
    s1 = Score("홍길동", 90 ,  80,70)
    s2 = Score("정길동",   50,    60 ,  70)
    s3 = Score("이길동", 100, 100,   100)
    s4 = Score()
    s5 = Score("박길동")

    print(s1); print(s2); print(s3); print(s4); print(s5, "그냥 안봄")
    #print(f"name = {s1.name} kor = {s1.kor} eng = {s1.eng} mat= {s1.mat}")
    #print(f"name = {s2.name} kor = {s2.kor} eng = {s2.eng} mat= {s2.mat}")
    #print(f"name = {s3.name} kor = {s3.kor} eng = {s3.eng} mat= {s3.mat}")

