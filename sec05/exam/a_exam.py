# 상속 관계를 통해서 후손을 통한 객체를 생성하고 후손의 객체를 통해서
# 선조의 메소드와 후손의 메소드를 자유롭게 호출할 수 있다.
class 선조:
    def prn(self):
        print("선조의 prn")

class 후손(선조):
    def my_print(self):
        print("후손의 my_print")

if __name__ == "__main__":
    print("============1. 후손을 통해 선조의 매소드를 토출===============")
    a1 = 후손()
    a7 = 선조()
    a1.my_print()# 후손의 객체를 통해서 선조의 메서드와 후손의 메소드를 자유롭게 호출해보자
    a1.prn()
    print(a1)
    print(a7)

    print("============1. 후손을 통해 선조의 매소드를 토출===============")


    print("============1. 후손을 통해 선조의 매소드를 토출===============")
