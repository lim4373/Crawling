class Test:
    pass
class Test01:
   def __init__(self):
       print("명시된 기본 생성자야")
class Test02:
   def __init__(self, a, b):
       print("명시된 값을 받는 생성자야" ,a,b )
if __name__ == '__main__':
    print(Test())  # init -> repr -> 기본(default)생성자호출
    Test01(); Test01(); Test01()  #명시된 기본 생성자 호출
    Test02(1,1);     Test02(2,2);    Test02(3,3)   #명시된 매개 인자 받는 생성자 호출
