def Test01():
    for i in range(1, 4):# 행의 값 1~3
        #print(f"=={i}==")
        for j in range(1, 4):# 열의 값 1~3
            #print(f"=={j}==")
            print(f"({i}, {j})", end = ' ')
        print()
def Test02():
    start_num = 1
    #start_num = 25
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix += f"{start_num}\t"
            start_num += 1
            #start_num -= 1
        matrix += "\n"
    print(matrix)


def Test03():
    #start_num = 1
    start_num = 25
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix += f"{start_num}\t"
            #start_num += 1
            start_num -= 1
        matrix += "\n"
    print(matrix)
#matploblibrary 로 만들어보고 만들어오기
def Test04():
    for i in range(2, 10,2):
        print(f'=== {i} 단 ==')
        for j in range(2, 9, 2):
            #print ("%d * %d = \t" %(i, j), i*j)
            print(f"{i} * {j} = {i*j}")
        print(f'===========')
        
        
if __name__ == '__main__':
    Test03()
        
        
        
        