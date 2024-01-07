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

if __name__ == '__main__':
    #[2] 객체 생성
    t1= Test(100,200)  #t1.a =100, t1.b = 200
    #[3] 멤버호출
    print(f'{t1.a}  {t1.b}  ')
    t2  =  Test(300,400)
    print(f'{t2.a}  {t2.b}  ')
    t3=  Test(500,600)
    print(f'{t3.a}  {t3.b}  ')

    #t1.a를 3000으로 변경 후 출력
    t1.a =3000
    print(f'{t1.a}  {t1.b}  ')#3000, 200
    # 각 stack 객체의 t1,t2,t3 주소를 출력 해보자.
    print("t1의 주소  :" , id(t1))  #36
    print("t2의 주소  :", id(t2))   #84
    print("t3의 주소  :", id(t3))   #28

    # 각 heap 객체의  &Test(100,200), &Test(300,400), &Test(500,600)
    print(t1)  #<__main__.Test object at 0x000001637D113740> Test클래스는 __repr__없네
    print(t2)  #<__main__.Test object at 0x000001637D113770>
    print(t3)  #<__main__.Test object at 0x000001637D113800>

















