#객체간의 연산[산술, 관계, 비교 ] -> 사용자 객체정렬  을 구현하는 재정의 메소드
class MyClass:

    def __init__(self , value) -> None:
        self.value   = value

    def __add__(self, other):
        print("__add__")
        return self.value + other;

    def __radd__(self, other):
        print("__radd__:오른쪽 피연산자와 현재 객체를 더한 값을 반환")
        # a = Myclass(10); res  = 5+a; res -> 15
        return  other + self.value ;

    def __sub__(self, other):
        return self.value - other;

    def __gt__(self, other):
        return self.value > other.value

obj = MyClass(5)  # 숫자 하나 관리하는 클래스
obj01 =MyClass(10)
res = obj  > obj01
print(res)
hap = obj+ obj01
print(hap)
#res = obj  < obj01
#print(res , type(res))
#print(dir(obj))
# (MyClass(5) + MyClass(10)  - MyClass(20) )





