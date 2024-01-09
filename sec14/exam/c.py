from bs4 import BeautifulSoup
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')

# 주석과 문자열을 저장할 리스트 객체ㄷ