''''
홀수인 경우:어떤 정수 n에 대해서, n % 2의 결과가 1이면, n은 홀수
짝수인 경우:어떤 정수 n에 대해서, n % 2의 결과가 0이면, n은 짝수
정수의 배수 : 어떤 정수 n에 대해서, n % 배수의 결과가 0 일경우   n % 5  ==  0
'''
#홀수는 반복하러 가고 짝수는 출력
def Test():
    for i in range(10):  #0 ~  9    range(stop)
                if i % 2 != 0: #i 를 2로 나눈 나머지가 0 아닌경우
                            continue # 반복을 계속하자
                print("%5d"%i,end="")


def Test01():
    for i in range(1,102):
        if i % 2 == 0:
            print(i, end= ' ')

#1~101까지 3의 배수만 출력
def Test02():
    for i in range(1,102):
        if i % 3 == 0:
            print(i, end= ' ')


#1~101까지 2의 배수이면서(and) 3의 배수를 출력
def Test03():
    for i in range(1,102):
        if i % 6 == 0:
            #if i % 2 == 0 and i % 3 ==0:
            print(i, end= ' ')
#1~101까지 2의 배수이면서 5의 배수를 출력하고 갯수 출력
def Test04():
    count = 0
    for i in range(1,102):
        if i % 10 == 0:
            count+=1
    print(count, end= ' ')
def Test05():
    count = []
    for i in range(1,102):
        if i % 2 == 0 and i % 5 == 0:
            count.append(i)
    else:
        print(f"count = {len(count)}, value = {count}")


if __name__=="__main__":
    #1. 각 함수를 dict에다 지정한다.
    functions = { '1': Test01,
                  '2': Test02,
                  '3': Test03,
                  '4': Test04,
                  '5': Test05 }
    #2. input으로 입력 받는다.
    fun_num = input("함수에 해당하는 번호를 입력해봐:  ")
    #3. 입력받은 함수명으로 실행한다.
    if fun_num in functions:
        functions[fun_num]()
    else:
        print("번호 오류")