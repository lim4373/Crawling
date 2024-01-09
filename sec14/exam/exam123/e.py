from bs4 import BeautifulSoup

rel_soup = BeautifulSoup('<p>Back to the <a rel="index first">homepage</a></p>', 'html.parser')
print(rel_soup.a['rel'])# a태그의 rel값의 속성 값을 출력
# ['index', 'first']
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>


print("1. 위 문서에 <a href =<li><a href=https://www.example.com>Example 1</a> 를 new_tag로추가해보자.")
new_a_tag = rel_soup.new_tag('a', href='https://www.example.com')
new_a_tag.string = "Example 1"
rel_soup.p.append(new_a_tag)
print("추가")
print(rel_soup)
print("=========")
print(rel_soup.p)

print("2. 위 문서에서 a가 가진 주소만 리턴해보자. find_all")
# object의 속성(attribute) 존재를 확인한다
hrefs = [a['href'] for a in rel_soup.find_all('a') if a.has_attr("href")]
print(hrefs)
"""
rel_soup.find_all('a')는 BeautifulSoup에서 'a' 태그를 모두 찾아서 리스트로 반환합니다. 여기서 'a' 태그는 하이퍼링크를 나타냅니다. 그 다음 부분 if a.has_attr("href")는 해당 'a' 태그가 'href' 속성을 가지고 있는지 확인합니다. 'href' 속성은 하이퍼링크의 목적지 URL을 정의하는 속성이며, 이 속성이 없는 경우는 걸러내기 위해 사용됩니다.

마지막 부분 [a['href'] for a in rel_soup.find_all('a') if a.has_attr("href")]는 리스트 컴프리헨션을 사용하여 'a' 태그 중에서 'href' 속성을 가진 것들의 값을 추출하여 리스트로 만듭니다."""
print("3. 위 문서에서 a가 가진 문자들만 추출해보자.find_all") #"get_text() 요소의 텍스트 내용 추출"
texts = [ a.get_text() for a in rel_soup.find_all('a')]
print(texts)