#1. olview.html 파일을 로드해서 soup 객체를 생성한다.

from bs4 import BeautifulSoup
# import olview.html
# 파일 이름에 따라 수정해주세요.
# file_name = 'sec14/exam/sec03/olview.html'

# olview.html 파일을 읽어와서 BeautifulSoup 객체를 생성합니다.
with open('C:\\python\\Project32\\sec14\\exam02\\sec03\\olview.html',encoding='utf-8') as fp:
    soup = BeautifulSoup(fp,'html.parser')
# print(soup.prettify())


# 2. 모든 <ol> 태그를 추출하자
# ol_tag = soup.find_all('ol')
# print(ol_tag)
#
# for ol in ol_tag:
#     print(ol.prettify())

#3. <ol> 태그 중 속성이 type "a"만 추출해보자.
res = soup.find_all('ol',{'type':'a'}) #리스트로 반환됨
print("이거",res)
for ol in res:
    print(ol)

print("4번")
#4. <ol> 태그 중 속성이 type "A"의 li만 추출해보자.
res1 = soup.find_all('ol',{'type':'A'})

li_text = [li.get_text()  for ol in res1 for li in ol.find_all('li')]
for ol1 in li_text:
    print(ol1)