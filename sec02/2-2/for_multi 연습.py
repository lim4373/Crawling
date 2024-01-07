
def Test():
    start_num = 1
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix += f"{start_num}\t"
            start_num += 1
        matrix += "\n"
    print(matrix)


def Test01():
    # start_num = 5*i+(j+1)
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix += f"{5*j+(i+1)}\t"
        matrix += "\n"
    print(matrix)


def Test02():
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix += f"{25-i-5*j}\t"
        matrix += "\n"
    print(matrix)


def Test03():
    start_num = 1
    matrix = ""
    for i in range(5):
        for j in range(5):
            if i == 2 or j == 2:
                matrix += f"*\t"
            else:
                matrix += f"{start_num}\t"
            start_num += 1
        matrix += "\n"
    print(matrix)


def Test04():
    start_num = 1
    matrix = ""
    for i in range(5):
        for j in range(5):
            if i == 0 or i == 4 or j == 0 or j == 4:
                matrix += f"*\t"
            else:
                matrix += f"{start_num}\t"
            start_num += 1
        matrix += "\n"
    print(matrix)




if __name__ == '__main__':
    Test03()