'''
   a,b라는 변수를 Test라는 이름의 자료형을 등록하고 싶다.
   선언  -> 객체생성  -> 멤버호출  (값전달 및 변경 리턴)
         a    b   --------- Test
        100 200     t1
        300 400     t2
        500 600     t3
'''
# [1]  선언
class Test:
     # 변수를 선언하고 초기화 하는 메소드 ( 생성자 )  -> 객체를 생성할 때 단 한번만 호출된다. / 명시호출하지 않는다
    def __init__(self, a,b):
        self.a= a
        self.b= b

    def __repr__(self):  #객체 변수를 호출할 때 자동으로 호출 된다.
        return f'{self.a}  {self.b} '


if __name__ == '__main__':

    t1= Test(100,200)  # 생성자 자동 호출 객체 생성
    t2 = Test(300,400)
    t3= Test(500,600)
    print(t1.__repr__())  # __repr__ 자동 호출 하면서 출력될 멤버 값을 리턴 한다.
    print(t2)
    print(t3)
    print(dir(t1))
















