from abc import abstractmethod, ABCMeta


class AA(metaclass=ABCMeta):
    def prn(self):
        pass

class AA:
    def prn(self):
        print("AA's method")
class BB(AA):
    def prn(self):
        print("BB's method")

class DD(AA):
    def prn(self):
        print("DD's method")




def my_call(res: AA):
    res.prn()


def test(a: AA): #데이터 타입을 명시
    pass

if __name__=="__main__":
    #my_call(AA())
    my_call(BB())
    my_call(DD())