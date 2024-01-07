class Test02:
   def __init__(self, a=0, b=0):
       self.a = a
       self.b = b
   def __repr__(self):
       return f' a ={self.a} b={self.b}'

if __name__ == '__main__':
    t1=Test02() #  a=0, b=0
    print(Test02(100)); # a=100, b=0
    print(Test02(50,50)) # a=50, b=50
    t1.a = 1000
    print(t1)