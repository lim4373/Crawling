#print("출력서식")  -> page 40 
import datetime  # 날짜 시간 모듈
import math
def case01():
    #정수 %d, 실수%f, 문자열 %s각 10자리씩 출력해보자.
    print("%10d %5d"%(100 , 200) )  #전체 정수 10자리 확보 후 100을 출력 , 5자리 확보후 200  
    print("%-5d %5d %5.1f"%(1,2,3.88888)) #1을 정수 5자리 확보 왼쪽정렬, , 2 정수 5자리 확보 후 출력
    print("%10s : %10s "%("aaaaaa","bbbbbbbbbbbbbbbbbbb"))
    ##  정수, 8진수, 16진수  
    print("%d %o %x %5f"%(100,100,100,3.14)) #소수점 기본정밀도 자리가 출력

def case02():
    #str's format ->  S.format(*args, **kwargs) -> str *튜플, *딕셔너리
     print("{0} {1}".format( "apple", 7.77 ) )
     print("{1} {0}".format( "apple", 7.77 ) )
     print("{0} {0}".format( "apple", 7.77 ) )
     print("{0:^10s} {1:10f}".format( "apple", 7.77 ) )
     print("{1} {1} {1}".format( "apple", 7.77 ) )
 
def case03():
    #str.format() 정수활용해 보자 . 
    num =42
    num01 = 100
    f= "The number is {0},{1}".format(num,num01)
    d= f"The number is {num}"
    print(f)
    print(d)

def case04():
    #str.format() 실수활용해 보자 . 
    pi=3.14159
    f= "The number is {: .2f}, {: .2f}".format(pi,math.pi) #소수 2번째 자리 까지
    print(f)
    
def case05():
    #str.format() 제로패딩 활용해 보자 . -> 수치 데이터 -> 저장대상 -> 0으로 채워서 저장 하고 싶을때
    # 2wlsghk, bin(value) -> int(
    num =42
    f= "The number is {:010d}".format(num)
    print(f,type(f))

    f= "Binary is {:b}".format(num)
    print(f,type(f))
    
def case06():  
    #날짜서식 date(year, month, day) --> date object
    date  = datetime.date(2023,7,7)
    date_1= datetime.datetime.today()
    f= "Date : {: %Y-%m-%d}".format(date)
    t = "Today : {:%Y-%m-%d}".format(date_1)
    print("======= today() 리턴값을 가지고 {: %Y-%m-%d}으로 출력을 해보자.========= ")
    print(f)
    print(t)
    '''
    datetime 모듈에 datetime클래스의 today 함수와 now()=(각자국가별 시간) 함수는 timezone에 따라 달라진다.
    1. datetime.datetime.today(): 현재 로컬기반으로 datetime객체를 리턴 한다.( 로컬 시간대 적용)
                                    - 로컬시간대와 상관없이 사용된다.
    2. datetime.datetime.now() : 현재 로컬기반으로 datetime 객체를 리턴 한다.(컴퓨터시간대 적용)
    '''

def case07():
    #튜플 -> * 
    point=(1,2,3,4)
    point_01=(11,2,3,4)
    f= "Point: (  {},{},{},{},{},{},{},{} )".format(*point, *point_01)
    print(f)
    a,b,*c = 1,2,3,4,5,6,7
    print(a,b,c, type(c))

def case08():
    #사전형dict **  
    person={'name':'홍길동' ,'age77':20}
    f="person : Name:{name} , age:{age77}".format(**person)
    print(f)
    

def case09():
    #인수위치  
    f=" {0} {1} {2}" .format(1,2,3)
    print(f)

if __name__ == '__main__':
    case09()




