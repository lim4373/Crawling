from inspect import  *
class 선조:
    def prn(self):
        print("선조의 prn")

class 후손(선조):
    def prn(self):
        super().prn()
        print("후손의 prn")


class MyClass(후손):
    def prn(self):
        super().prn()
        print("Myclass Prn")

if __name__ == "__main__":
    print("============4. 후손을 통해 선조의 매소드를 토출===============")
    s2 = MyClass()
    s2.prn()
    print("1. 클래스 객체 확인  :", getmro(MyClass))
    print("2. 매개인자 확인  :", getfullargspec(MyClass))
    print("3. 계층관계 : ", getmro(MyClass))
    print("4, 모듈확인  :", ismodule(MyClass))
    print("5. 멤버 확인  :", getmembers(MyClass))