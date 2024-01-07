
def  case01():
    try:
     res  = 10/2
    except  ZeroDivisionError as  ZDE  : #pvm에서 Error의 종류에 해당하는 클래스를 생성해서 리턴되는 것을 except에서 해결한다
        print(" 0으로 나누려고 했잖아 ")
    else :
        print("else")
    finally:
        print("오류 상관없이 반드시 수행할 명령  : 백업파일, 디비close() , 로그아웃  ")

    print( "===========case01============")
def case02():
    L= [1,2,3]
    try:
        num = L[4]
    except IndexError as IE:
        print("list index out of range" )  #  IndexError  : list index out of range
        print("IE =============> ",  IE , type(IE))
        IE.with_traceback("abc")
        num = L[0] #예외 처리
    else :
        print("else")
    finally:
        print("오류 상관없이 반드시 수행할 명령  : 백업파일, 디비close() , 로그아웃  ")
    print(num)



if __name__ == '__main__':
    case02()