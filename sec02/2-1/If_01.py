def If_test():
    my_id= input("Enter your id: ")

    if my_id == "1234":  # 값 비교
        print("true:", my_id)

#print("===================")
def If_test03(): # > < >= <= == !=  -> bool
    my_id= input("Enter your id: ")

    if my_id != "1234":  # 값 비교
        print("true:", my_id)

def If_test04():
    if None:#True None는 etc로 간다,,,,
        print("abc")
    elif False:
        print("False")
    else:
        print("etc....")

if __name__=='__main__':
    If_test04()
#my_id= input("Enter your id: ")
#while True:
#    if my_id == "a1234":  # 값 비교
    #    print("로그인 환영")
        #break
    #else:
     #   print("틀렸습니다")
      #  break
