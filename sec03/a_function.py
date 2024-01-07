x = 10 # G에 해당 전역변수
y = 11
print(id(x))
def foo():
    x = 20 # foo함수의 L에 해당, bar함수의 E에 해당 지역변수?
    print("foo's X=",x , id(x))
    def bar():
      a = 30 # L에 해당
      print( a, x, y ) # 각 변수는 L, E, G에 해당
    bar()
    x = 40
    bar()
def test():
    x =2000
    print("test's X=", x, id(x))

#https://gr-st-dev.tistory.com/875
if __name__ == '__main__':
    foo()
    #test()
    #print("X=",x,id(x))
    #pass