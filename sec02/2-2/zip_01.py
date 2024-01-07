
#목록을 한꺼 번에 묶어서 리턴 1,10: 2,20: 3,30으로 리턴된다.  
# zip ( ,,,,,)  ->for로 풀어낸다.  
#목록에서 가장 짧은 객체를 기준으로 페어를 만든다. 
def Test():
        for x, y ,z in zip ([print("111"), 2, 3,4,5], [10, 20, 30, 40, None ],[11, 20, 33, print("333"), None  ] ) :
                print (f'{x}  :   {y}  : {z}' )
        

#목록을 묶어서 set으로 리턴 
def Test01():
        s = {1, 5, 1, 1, 1, 3, 7}
        d = set([1, 3, 5, 7])
        print("====> ", set(zip ( ['a', 'b', 'c','d'], [1, 2, 3,4])))
        res = set(zip(['a','b','c','d'],[1,2,3,4]))
        print(type(res))
        print(res)
        print(s)
        print(d)


#목록을 묶어서 dict로 리턴
def Test02():
        keys = ['cat', 'dog', 'duck']
        values = ['야옹', '멍멍', '꽥꽥']
        print (dict(zip(keys, values)))

if __name__ == "__main__":
        Test02()