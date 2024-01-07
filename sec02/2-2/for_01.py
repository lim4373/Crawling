#fruit  = ['apple','watermelon','peach','pear']

#if "apple" in fruit or len(fruit) > 5 :
#	for m_f in fruit:
#		print(m_f)


#True
# and로 하면 둘 다 맞아야해서 안 나옴

def for_test01(): # 리스트
	for res in [1,2,3,4]:
		print(f'{res}', end= ' ')


def for_test02(): #튜플
	for res in (1,2,3,4):
		print(f'{res}', end= ' ')

def for_test03():
	print(range(10),list(range(10)),list(range(0,101,2)))

	for i in range(10):
		print(f'{i}', end= ' ')

def for_test04():
	# 0~100 까지 정수 , 5의 배수만 출력 하고 싶다. range()와 for를 사용해서 출력
	for i in range(1,101): # for x in range(0,101,5):
		if i%5 == 0:
			print(i, end =' ')
	print("\n=====================================\n")
	for i in range(100,-1,-1):
		print(i, end=' ')


def for_test06():
	fruit = ['apple', 'watermelon', 'peach', 'pear']

	if "apple" in fruit or len(fruit) > 5:
		for m_f in fruit:
			print(m_f)

if __name__=="__main__":
	#for_test04()
	for s in 'abcde':
		print(s , end = '')