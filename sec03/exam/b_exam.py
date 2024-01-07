def myFunc(*a): # 튜플로 출력
    print(a)

def myFunc01(*a,b=10): # 튜플로 출력
    print(f"a = {a}  b = {b} ")



def myFunc02(*a,**d): # 튜플로 출력  *이거 찾아보기
    print(f"tuple = {a}  dict = {d} ")

def myFunc03(*a,b=10,**d): # 튜플로 출력
    print(f"a = {a}  b = {b} dict= {d} ")

if __name__ == "__main__":
    '''
    #myFunc01(1,2,3,4,5, b =100)
    #myFunc01(1)
    #myFunc02(1,2,3,4, z=100, y=200)
    mytuple = (1,2,3,4,5)
    mydict = { 'a':1, 'b': 2}
    myFunc02(mytuple,**mydict)
    '''
    myFunc03(1,2,3, b=4,z=100,y=200)