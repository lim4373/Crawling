class MyValue: # 클래스 변수와 인스턴스 변수에 각각 +i를 한 결과를 비교
    shard_value = 0 # 클래스 변수
    def __init__(self,value):
        self.value = value
    def add_shard_value(self):
        MyValue.shard_value +=1

    def view(self):
        print(f"instance value  {self.value}, shard_value = { MyValue.shard_value}")


if __name__ =="__main__":
    ob1 = MyValue(10)
    ob2 = MyValue(20)
    ob1.add_shard_value()# 클래스 변수값이 증가
    ob1.view()
    ob2.view()