from  collections import defaultdict
#dict를 선언하고
def case01():
      artist  =['나얼','박효신',   '손석구' ]
      music =[ '가을아침','눈의꽃', '나의 해방일지']
      res  = defaultdict(list) # 기본 dict를 만들고  키 , 밸류로 생성된 것을 추가해서 출력 해보자 .
      #dict로 생성
      for i, k in enumerate(artist):
          res[k].append(music[i])
      for i in res.values():
          print(i)
      pass

def case02():
    counter  = defaultdict(int) # 찾아보기
    print(counter)
    my_list  =  [1,2,3,4,5]
    for num in  my_list:
        counter[num] +=1.5
    for num, count  in counter.items():
        print(f' {num} : {count}' )

if __name__ == '__main__':
    case01()
    print("========================")
    case02()