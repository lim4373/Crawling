from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<table>
<caption> mylist </caption>
<thead>
<tr> <th>Name</th><th>Age</th>
  <th>City</th>
</tr>
</thead>
<tbody>
<tr>
  <td>John</td> <td>25</td> <td>New York</td> </tr>
<tr>
  <td>Alice</td> <td>30</td> <td>London</td> </tr>
</tbody>
</table>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# 1. 테이블의 제목인 thead의 문자열만 출력
thead_text = soup.thead.get_text().strip()
print("1. thead의 문자열:", thead_text)

# 2. tbody의 문자열만 출력
tbody_text = soup.tbody.text.strip()
print("2. tbody의 문자열:", tbody_text)


tbody_text = soup.tbody.text
print("2. tbody의 문자열:", tbody_text)

# 3. 1,2 번으로 추출한 내용을 가지고 caption의 문자열을 파일명으로 지정해서 mylist.txt로 저장
# temp = soup.caption.get_text().strip() + '.txt'
# with open(temp,'w') as f:
#     for string in list1:
#         f.write(string+',')
#     f.write('\n')
#     for string in list2:
#         f.write(string +',')

temp = soup.caption.get_text().strip() + '.txt'
with open(temp,'w') as f:
    f.write(thead_text + "\n"+ tbody_text)