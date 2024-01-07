# 상속 관계를 통해서 후손을 통한 객체를 생성하고 후손의 객체를 통해서 [생성자 구문을 확인하고]
# 선조의 메소드와 후손의 메소드를 자유롭게 호출할 수 있다.
# 생성자를 통해서 값전달을 해보자. 선조(a)
class 선조:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def prn(self):
        print("선조의 prn")

class 후손(선조):
    def __init__(self,a,b):
        super().__init__(a,b)

    def my_print(self):
        print("후손의 my_print")
        print("상속된 선조의 변수 a:",  self.a)
        print("상속된 선조의 변수 b:", self.b)

if __name__ == "__main__":
    print("============3. 후손을 통해서 생성자와 선조의 매소드를 토출===============")
    a1 = 후손(100,200)
    a1.my_print()# 후손의 메소드 호출
    a1.prn() # 선조의 메소드 호출


    a2 = 후손(400,500)
    a2.prn()
    a1.my_print()
