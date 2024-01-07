#슬라이싱
#객체[start: end-1 : step ]
mystring = "hello world!"

print(mystring[0]) #h
print(mystring[0:12:3])
print(mystring[1]) # e
print(mystring[2]) # l
print(mystring[-1])# !
print(mystring[11])# !
print("mystring's count =",len(mystring))
print(f"mystring's count ={len(mystring)}")

a= 100
b=200
print(f"{a}+\t+{b}={a+b}")