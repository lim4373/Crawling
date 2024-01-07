''''

1. MyScore :
score : 이름, 국어 영어 수학 종점 평균 출력 메소드
MyScore : Score를 상속받아 5과목 국어 영어 수학 음악 체육 (muse,pe)를 총 평균 학점

2. sec04_1.exam.Score에서 호출을 해서 객체 배열을 만들엇 접근해 보자
'''
from sec04_1.exam.Score import  *
class MyScore(Score):
    def __init__(self, name, kor, eng, mat, muse, pe) -> None:  # 객체를 생성할 때 값을 받으면서 생성 하겠다.(초기값을 자동으로 생성하지 않고 받아서 초기화)
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.muse = muse
        self.pe = pe

    def getTot(self):
        return self.kor + self.eng + self.mat + self.muse + self.pe

    def getAvg(self):
            # return #(self.kor + self.eng+ self.mat)/3
        return self.getTot() // 5

    def getGrade(self):  # 임의로 함
        avg = self.getAvg()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
if __name__ == '__main__':
    my_list  =  [MyScore ('홍길동1' ,100,100,100,80,80) ,
                 MyScore ('홍길동2' ,90,90,90,80,80),
                 MyScore ('홍길동3' ,80,80,80,80,80)]
    list(map(lambda x:print(x), my_list))
    #홍길동1의 국어점수를 50을 변경후 전체 출력해보자
    #for res  in my_list:
     #   if res.getName() =='홍길동1':
      #      res.setKor(50)
       #     print(res)
        #else:
         #   print(res)
    print("===========================================")
    s1 = Score("홍길동", 90, 80, 70, 80, 80)
    s2 = Score("정길동", 50, 60, 70, 80, 80)
    s3 = Score("이길동", 100, 100, 100, 80, 80)

    print(f'{s1.name} {s1.kor} {s1.eng} {s1.mat} {s1.muse} {s1.pe} {s1.getTot()} {s1.getAvg()} {s1.getGrade()}')
    print(f'{s2.name} {s2.kor} {s2.eng} {s2.mat} {s2.muse} {s2.pe} {s2.getTot()} {s2.getAvg()} {s2.getGrade()}')
    print(f'{s3.name} {s3.kor} {s3.eng} {s3.mat} {s3.muse} {s3.pe} {s3.getTot()} {s3.getAvg()} {s3.getGrade()}')

