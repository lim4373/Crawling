import keyword
#1.일반데이터 타입  
a = 10
b= 98.0
c= "abc"
d="한글이야"

print(a,b,c,d)
print(type(a),type(b),type(c),type(d))
#print(a+b+c+d)
print(c+d)
print(str(a)+str(b)+"\t"+c+"\n"+d)

#2. 키워드 확인  
print(dir(keyword))

print(keyword.kwlist)
print(keyword.softkwlist)




