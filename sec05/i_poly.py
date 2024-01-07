from sec04_1.exam.Mycalc import Calc



if __name__ == '__main__':
     #c1 = Calc(100,50)
     #print(c1)

     mlist =[Calc(100,50),Calc(200,150),Calc(300,250)]
     #a의 값이 100인값을 찾아서 777 바꾼 후 출력 하자

     print("====================")
     for x in mlist:
          print(x)

     # b 값이 150인값을 찾아서 888  바꾼 후 출력 하자
     mlist = list(map(lambda x: Calc(x.a, 888) if x.b == 150 else x, mlist ))
     for x in mlist:
          print(x)
          print("================================================")


#a의 값이 100인값을 찾아서 777 바꾼 후 출력 하자
     mlist = list(map(lambda x: Calc(777, x.b) if x.a == 100 else x, mlist))

     for x in mlist:
          print(x)
