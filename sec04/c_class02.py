
class Test02():
    def __init__(self,a=0,b=0):
        #print("명시된 기본 생성자야",a,b)
        self.a = a
        self.b = b
        pass
    def __repr__(self):
        return f"a = {self.a} b = {self.b}"



if __name__ =="__main__":
    t1 = Test02()
    print(Test02()) # a= 0 , b= 0
    print(Test02(100));# a = 100, b = 0
    print(Test02(50,50))#  a=50, b=50
    t1.a = 1000
    print(t1)