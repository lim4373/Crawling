#팩토리얼 계산 , 피보나치 수열 풀어보기 숙제, 하노이탑, 재귀함수
# 람다?
def factorial(n):
    print(f'==========={n}')
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


#피보나치 수열: 이전 두 숫자의 합이 현재 숫자가 되는 수열
# 수열: 일반항 , 유한, 무한 , 수열의 종류(아열된 원소의 정렬), 등차수열, 등비수열, 피보나치 수열
def fibo(n):
    if n<= 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


if __name__ == '__main__':
    res=fibo(10)
    print("피보나치 수열의 10번째 값:",res)