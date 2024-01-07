'''
a,b라는 변수를 Test라는 이름의 자료형을 등록하고 싶다.
 선언 -> 객체생성 -> 멤버호출( 값 전달 및 변경 리턴)
                a   b ---------- Test
                100 200            t1
                300 400             t2
                500 600             t3

'''
#선언
# this: 현재 오브젝트를 지칭하는 연산자
# self: 현재 오브젝트를 지칭하는 변수
class Test: # class 강의 찾아보기, # 변수를 선언하고 초기화 하는 메소드(생성자) -> 객체를 생성할 때 단 한번만 호출된다. / 명시 호출하지 않는다
    #https://engineer-mole.tistory.com/190
    #int a
    #int b 나만의 자료형 만들기
    # 변수를 선언하고 초기화 하는 메소드
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __repr__(self): # 객체 변수를 호출할 때 자동으로 호출된다.
        return f"{self.a} {self.b}"


if __name__ =="__main__":
    # 객체 생성은 2개
    t1 = Test(100,200) #t1.a = 100, t1.b = 200
   # print(f"{t1.a} {t1.b}")
    #print("=================================")
    t2 = Test(300,400)
    #print(f"{t2.a} {t2.b}")
    #print("=================================")
    t3 = Test (500,600)
    #print(f"{t3.a} {t3.b}")
    #print("=================================")

    #t1.a= 3000
    #print(f"{t1.a} {t1.b}")
    #print("=================================")


    # 각 객체의 주소를 출력 해보자.
    #print("t1의 주소:", id(t1)) # 80
    #print("t2의 주소:", id(t2)) # 20
    #print("t3의 주소:", id(t3)) # 68
    #print("=================================")

    # 각 heap 객체의 Test(100,200), Test2(300,400) ,Test3(500,600)
    print(t1) # 100 각기 다른 주소, __repr__ w자동 호출 하면서 출력 될 멤버 값을 리턴 한다.
    print(t2)
    print(t3)
    print(dir(t1))
    print("=======================01. 객체 배열 _시퀀스형=====================")
    test_all = [Test(100,200),Test(300,400), Test(300,400)]
    print(test_all[0], test_all[1], test_all[2])# 인덱스 명시호출
    for res in test_all:
        print(res)

    print("===================02.리스트 언패킹 =========================")
    test_all = [Test(100, 200), Test(300, 400), Test(300, 400)]
    print(*test_all)

    print("===================03.람다식 =========================")
    '''
    test_all = [Test(100, 200), Test(300, 400), Test(300, 400)]
    for res in test_all:
        print(res)
    '''
    list(map(lambda res: print(res), test_all))

    print("===================04.번외편 =========================")
    my_array = [1,2,3,4,5,6,7,8,9,10]
    list(map(lambda ar:print(f"{ar*2}", end = ' '),my_array))
