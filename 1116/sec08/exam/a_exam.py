#apple.jpg를 읽어서 apple_cpoy.png로 저장을 해보자.


# 파일을 읽어서 
with open("../apple.jpg",'rb')  as f:
    res = f.read()


# 파일을 저장하자
print("=============read=========================")
with open("apple_cpoy.jpg",'wb')  as f:
    f.write(res)
    
    
    
    
    
    
    
# 파일을 저장하자