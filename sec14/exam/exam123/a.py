from bs4 import BeautifulSoup

# 가져온 문서로 파씽
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.html.body.a['class'])
# print(soup.html.body.a['href'])
# print(soup.html.body.a['id'],"이거")
# print("=================")
print(soup.html.body.p.text)
# <a></a>는 하이퍼링크를 걸어주는 태그
# for link in soup.find_all("a"):
#     print(link.get('href')) # href는 링크된 페이지 url을 명시한 곳
#
# print(soup.get_text()) #조금 더 정확히 표현하면 get_text() 메서드는 현재 태그를 포함하여 모든 하위 태그를 제거하고 유니코드 텍스트만 들어있는 문자열을 반환합니다.
#
# print(soup.find('p'))
# print(soup.find('p').text)
#
#
# res= soup.findAll('a')
# for m_res in res:
#     print(m_res)


res= soup.findAll('a')
for m_res in res:
    print(f"{m_res.text} \t{m_res['href']}")

