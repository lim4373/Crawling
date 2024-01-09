from bs4 import BeautifulSoup
#1. olview.html 파일을 로드해서 soup 객체를 생성한다.
with open('C:\\python\\Project32\\sec14\\exam02\\sec03\\olview02.html', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
# print(soup.prettify())
# a= soup.find_all(True)
# print(a)
css_classes =set() #클래스를 담을 변수
css_id = set() #id를 담을 변수

#모든 css를  탐색 select("*")
for tag in soup.select("*"):
# 클래스 속성이 있는 경우 값을 추출해서 저장 'class' in tag.attrs:
    if 'class' in tag.attrs:
        css_classes.update(tag['class'])
# id속성이 있는 경우 값을 추출해서 저장
    if 'id' in tag.attrs:
        css_id.add(tag['id'])

print("css_classes:", css_classes)
print("css_id",css_id )