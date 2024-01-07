'''  Address
name    addr    tel
이름     주소   전화번호
홍길동   서울   02-0000
정길동   인천    031-0000
최길동   나주    063-0000
'''
########Address 클래스 선언
class Address:
    def __init__(self,name, addr, tel ) -> None:  #객체 생성 멤버 초기화
        self.name = name
        self.addr  = addr
        self.tel   = tel

    def __repr__(self) -> str:
        return  f'{self.name:^10s} {self.addr:^10s}{self.tel:^10s}'


if __name__ == '__main__':
     print( "1.  전체 출력  ")
     address_all = [Address('홍길동', '서울', '02-0000'),  #address_all[0]
                    Address('정길동', '인천', '031-0000'), #address_all[1]
                    Address('최길동', '나주', '063-0000')] #address_all[2]

     list(map(lambda x:print(x) , address_all))

     print("2.주소록 에서 홍길동의 이름을 찾아서 주소를 광주로 변형 후 전체 출력   ")
     def update(x):
         if x.name=='홍길동':
             x.addr = '광주'
         print(x)
         return x
     list(map(update, address_all))
     print("==========[홍길동 레코드만 추출 map ]=====================================")
     list(map(lambda x: print(x) if x.name =="홍길동" else None, address_all))

     print("==========[홍길동 레코드만 추출 filter(function(bool),iter) ]=====================================")
     def find_filter(x):
         if x.name=='홍길동':
           print(x)
           return True
         return False

     list(filter(find_filter, address_all))

     list(filter(lambda x: (print(x), True) if x.name == "홍길동" else (None, False), address_all))



     print("3.주소록 에서 정길동의 전화번호를  77777 변형 후 전체 출력   ")
     print("4.최길동의 이름을 박길동 변형 후 전체 출력   ")
     print("5.주소록 에서 홍길동의 전화번호를 02-8888 전체출력     ")
     print("6.주소록 에서 정길동의  주소는 '제주도' 전화번호를 064 -0000 변경 후 전체 출력    ")
