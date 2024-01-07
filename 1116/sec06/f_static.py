
class Test:
    @staticmethod
    def get_hap(a,b):
        return a+b

    @classmethod
    def get_mul(self,a,b):
        return a*b

if __name__ == '__main__':
    print( Test.get_hap(10,10))
    print(Test.get_mul(10, 10))

    #호출은 되지만 영역은 다르게 바운드 되고  Test.get_hap(10,10) 생각하고 컴파일된다.
    t1  = Test()
    print(t1.get_hap(1,2))    # X