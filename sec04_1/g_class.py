class MyClass:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"__str__={self.name}"

    def __repr__(self):
        return f"__repr__ = {self.name}"



if __name__=="__main__":
    obj = MyClass("홍길동")
    print(str(obj))
    print(repr(obj))
    print(obj)