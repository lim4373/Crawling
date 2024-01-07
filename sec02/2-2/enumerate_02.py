
#enumerate()함수 미사용 한 경우
fruit  = ['apple','watermelon','peach','pear']
for i in range(len(fruit)):
   print(i+100, fruit[i])


print('--------------------------')
#enumerate()함수 사용 한 경우
for i, res in enumerate(fruit,100):
       print(i,res)


print('--------------------------')
#결과를 파일로 저장해보자.
with open('fortest.txt', 'w') as file:
    for i, res in enumerate(fruit,100):
        file.write(f"{i},{res} \n")
# 읽어들이기
with open('fortest.txt', 'r') as file:
    print(file.read())
