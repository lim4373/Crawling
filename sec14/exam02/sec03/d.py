from bs4 import BeautifulSoup
with open('C:\\python\\Project32\\sec14\\exam02\\sec03\\olview02.html',encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
# print(soup.prettify())

# for tag in soup.select('*'):
#     css_classes : {'b1','a1'}
#     class_id : {'e1','c1','d1'}

# # 1. id 중에 e1인 태그를 찾아서 값만 출력해보자. select_one()
# id_res = soup.select_one('#e1')
# if id_res:
#     print('1번')
#     print(id_res.get_text())
#
# #2 . class 중에 a1인 태그를 찾아서 값만 출력해보자.select()
# class_res = soup.select('.a1')
# for tag in class_res:
#     print('2번')
#     print(tag.get_text())

# 1. id 중에 e1인 태그를 찾아서 값만 출력해보자. select_one()
id_res1 = soup.select_one("#e1")
if id_res1:
    print("1번",id_res1.get_text())


# #2 . class 중에 a1인 태그를 찾아서 값만 출력해보자.select()
class_res = soup.select(".a1") #리스트 형태로 반환
for tag in class_res:
    print("2번",tag.get_text())
############## find all
# # 1. id 주에 e1인 태그를 찾아서 값만 출력해보자. find()
id_find1 = soup.find(id="e1")
if id_find1:
    print('find 1번')
    print(id_find1.get_text())

# #2 . class 중에 a1인 태그를 찾아서 값만 출력해보자. find_all()
id_find2 = soup.find_all(class_='a1')
for tag1 in id_find2:
    print(tag1.get_text())
############## find all
# # 1. id 주에 e1인 태그를 찾아서 값만 출력해보자. find()
# id_res = soup.find(id='e1')
# if id_res:
#     print('find 1번')
#     print(id_res.get_text())
#
# #2 . class 중에 a1인 태그를 찾아서 값만 출력해보자. find_all()
# class_res = soup.find_all(class_='a1')
# for tag in class_res:
#     print('find 2번')
#     print(tag.get_text())


