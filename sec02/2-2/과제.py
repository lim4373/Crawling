def test01():
    start_num = 1
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix +=f"{start_num}\t"
            start_num +=1
        matrix += "\n"
    print(matrix)

def test02():
    start_num = 25
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix +=f"{start_num}\t"
            start_num -=1
        matrix += "\n"
    print(matrix)

def test03():
    start_num = 1
    matrix = ""
    for i in range(5):
        for j in range(5):
            if  i == j:
                matrix += f"*\t"
            else:
                matrix +=f"{start_num}\t"
            start_num +=1
        matrix += "\n"
    print(matrix)

def test04(): #대각선
    start_num = 1
    matrix = ""
    for i in range(5):
        for j in range(5):
            if  i+j == 4:
                matrix += f"*\t"
            else:
                matrix +=f"{start_num}\t"
            start_num +=1
        matrix += "\n"
    print(matrix)

def test05():
    start_num = 1
    matrix = ""
    for i in range(5):
        for j in range(5):
            if  i == 0 or i == 4 or j == 0 or j==4:
                matrix += f"*\t"
            else:
                matrix +=f"{start_num}\t"
            start_num +=1
        matrix += "\n"
    print(matrix)

def test06(): # + 모양
    start_num = 1
    matrix = ""
    for i in range(5):
        for j in range(5):
            if  i == 2 or j==2:
                matrix += f"*\t"
            else:
                matrix +=f"{start_num}\t"
            start_num +=1
        matrix += "\n"
    print(matrix)

def test07():
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix += f"{5*j+(i+1)}\t"
        matrix += "\n"
    print(matrix)

def test08():
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix += f"{25-i-5*j}\t"
        matrix += "\n"
    print(matrix)

def test09():
    start_num = 1
    matrix = ""
    for i in range(5):
        for j in range(5):
            if  i ==3 and j == 2:
                matrix += f"*\t"
            else:
                matrix +=f"{start_num}\t"
            start_num +=1
        matrix += "\n"
    print(matrix)


if __name__ =="__main__":
    test01()


