def test():
    def my_inner():
        return 100
    return my_inner()


def test01(a):
    b=[1,2,3,4,5]
    def my_inner():
        return 100*a + b[a]
    return my_inner()

def quadratic( a, b, c ):
    cache = {}
    def f( x ):
        if x in cache:
            return cache[x]
        y = a * x * x + b * x + c
        cache[ x ] = y
        return y
    def mytest():
        return 99999
    return f
    #return mytest

def add(a):
    return a + b + c


def outer():
    x= 10
    def inner():
        return x
    return inner

if __name__=="__main__":
    #print(test())
    #res = test # 참조
    #print(res())
    #print(test01(3))
    f1 = quadratic(3,-4,5)
    print(f1)
    print(f1(3))
    #print(f1.__closure__,"-------------->", type(f1.__closure__))
    #print(f1.__closure__[0])
    res = [cell.cell_contents for cell in  f1.__closure__]
    print(res)