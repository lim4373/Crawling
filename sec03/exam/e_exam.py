from functools import reduce

def Test01_map():
    numbers = [1,2,3,4,5]
    res = map(lambda x:x*2, numbers)
    print(list(res))
def Test02_filter():
    numbers = [1, 2, 3, 4, 5]
    res = filter(lambda x: x % 2== 0 , numbers)
    print(list(res))


def Test03_reduce():
    numbers = [1, 2, 3, 4, 5]
    res = reduce(lambda x,y: x * y, numbers)
    print(res)


if __name__ == "__main__":
    Test01_map()
    Test02_filter()
    Test03_reduce()