from bs4 import BeautifulSoup

rel_soup = BeautifulSoup('<p>Back to the <a rel="index first">homepage</a></p>', 'html.parser')
print(rel_soup.a['rel'])
# ['index', 'first']
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>

print("1. 위 문서에 <a href =<li><a href=https://www.example.com>Example 1</a> 를 new_tag로추가해보자.")
new_a_tag = rel_soup.new_tag('a', href='https://www.example.com')
new_a_tag.string = 'Example 1'
rel_soup.p.append(new_a_tag)
print("변경된 태그")
print(rel_soup.p)

print("2. 위 문서에서 a가 가진 주소만 리턴해보자")

hrefs = [a['href'] for a in rel_soup.find_all('a') if a.has_attr("href")]
print("모든 <a> 태그의 href 속성값:")
print(hrefs)
# for i, a_tag in enumerate(all_a_tags[:5]):
#     href_value = a_tag.get('href')
#     print(f"{i+1}. <a> 태그의 주소: {href_value}")

print("3. 위 문서에서 a가 가진 문자들만 추출해보자.")
texts = [a.get_text() for a in rel_soup.find_all('a')]
print("모든 <a> 태그의 텍스트:")
print(texts)