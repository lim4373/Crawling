'''
 name   kor  eng  mat    => Score
홍길동   90    80   70    => s1
정길동   50    60   70    => s2
이길동   100  100   100   => s3
'''
# 클래스를 선언하게 되면 모든 클래스의 수퍼인 Object의 자식이 되서 기능및 변수등을 상속받게 된다.
class Score:# 클래스에서 멤버는 self
     def __init__(self,name,kor,eng,mat) -> None :    #객체를 생성할 때 값을 받으면서 생성 하겠다.(초기값을 자동으로 생성하지 않고 받아서 초기화)
           self.name  = name
           self.kor  =  kor
           self.eng  = eng
           self.mat  = mat

     def __repr__(self) -> str:  #  재정의
         return f'name ={self.name} kor={self.kor}  eng ={self.eng}  mat ={self.mat} '

if __name__ == '__main__':
    s1  = Score("홍길동",   90,    80,   70)
    s2 = Score("정길동", 50, 60, 70)
    s3 = Score("이길동", 100, 100, 100)

    print(s1)
    print(s2)
    print(s3)



