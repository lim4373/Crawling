# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
# soup = BeautifulSoup(response,"html.parser") #html 접근
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
#print(soup, type(soup))
# print(dir(soup))

print(soup.html.body.p)

print(soup.html.body.a['class'])
print(soup.html.body.a['href'])
print(soup.html.body.a['id'])
print(soup.html.body.p.text)


print(help(soup.find))

res = soup.findAll('a')
for m_res in res:
    print(m_res)

print("========================")

res = soup.findAll('a')
for m_res in res:
    print(f"{m_res.text}\t {m_res['href']}")