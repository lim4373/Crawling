def MyTest(a,b,c,d): #매개인자의 초기값이 없는 함수를 선언해서 호출할 경우 반드시 순서 및 변수명을 호출해서 값대입 호출
    print(a,b,c,d)

def MyTest02(a,b=2,c=0,d=0): # 초기값이 있을 경우 값전달 없이 호출 해도 된다.
    print(a,b,c,d)




if __name__=='__main__':
    #MyTest(b=2,a=1,c=3,d=4) # MyTest() 를 호출하게 되면 100을 리턴해서 출력하게 된다.
    MyTest02()
    MyTest02(100)
    MyTest02(100,200)
    MyTest02(a=1,d=3)