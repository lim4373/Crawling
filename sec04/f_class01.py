'''
이름    주소  전화번호
홍길동   서울   02-0000
정길동   인천    031-0000
최길동   나주    063-0000
'''

#############Address 클래스 선언
class Address():
    def __init__(self, name, addr, num)->None:
        self.name = name
        self.addr = addr
        self.num = num

    def __repr__(self) -> str:
            return f"{self.name:^10s}{self.addr:^10s}{self.num:^10s}"

if __name__ == "__main__":
    print("1. 전체 출력 ")
    #address1 = Address("홍길동", "서울", "02-0000")
    #address2 = Address("정길동", "인천", "031-0000")
    #address3 = Address("최길동", "나주", "063-0000")
    #address_all = [address1, address2, address3]

    address_all= [Address("홍길동", "서울", "02-0000"),
                  Address("정길동", "인천", "031-0000"),
                  Address("최길동", "나주", "063-0000")]
    list(map(lambda x:print(x), address_all))


    print("2. 주소록에서 홍길동의 이름을 찾아서 주소를 광주로 변경 후 전체 출력")
    for res in address_all:
        if res.name=="홍길동":
            res.addr= "광주"
            print(res)

