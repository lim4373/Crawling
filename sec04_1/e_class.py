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
    print("=========================case01.객체 배열 _시퀀스형 ================================")
    test_all = [Test(100,200),Test(300,400) ,Test(300,400)]
    print(test_all[0] , test_all[1], test_all[2])  # 인덱스 명시호출
    for res  in test_all: # 반복 전체 출력
        print(res)

    print("=========================case02.리스트 언팩킹 ================================")
    test_all = [Test(100, 200), Test(300, 400), Test(300, 400)]
    print(*test_all) #언팩킹

    print("=========================case03.람다식  ================================")
    test_all02 = [Test(100, 200), Test(300, 400), Test(300, 400)]
    list(map(lambda res02: print(res02) , test_all02 ))

    print("=========================case04.번외편  ================================")
    my_array  =  [1,2,3,4,5,6,7,8,9, 10]
    list(map(lambda ar: print(f'{ar*2}', end='\t' ) ,my_array))











