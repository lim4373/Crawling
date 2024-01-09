# import requests
from bs4 import BeautifulSoup
# 파씽: 어떠한 웹 페이지에서 내가 원하는 데이터를 특정 패턴이나 순서로 추출하여 정보를 가공하는 것
html_doc = 'https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106'
# response = requests.get(url)
soup = BeautifulSoup(html_doc , 'html.parser')

# 예시로 첫 번째 글만 가져옴
first_post = soup.select_one('.boardList-wrap tbody tr:first-child')

name = first_post.select_one('.board-name').text.strip()
date = first_post.select_one('.board-date').text.strip()
content = first_post.select_one('.board-content').text.strip()

print(f'이름: {name}\n날짜: {date}\n내용: {content}')
