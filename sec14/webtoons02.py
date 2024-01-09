from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

url = 'https://comic.naver.com/webtoon?tab=tue'
# ver 4.6 수동드라이버 x
# # service = webdriver.chrome.service.Service('./chromedriver.exe') #1. 크롬 드라이버 셋팅
# driver = webdriver.Chrome() #2. 브라우저 생성
driver = webdriver.Chrome()
sleep(10)
driver.get(url)  #브라우저 실행해서 url 요청을 한다.
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser') #파싱 객체 생성

li_list = soup.select('.component_wrap .item')
print(li_list)
for li in li_list:
    title = li.find('span', class_='ContentTitle__title--e3qXt').text
    star = li.find('span', class_='Rating__star_area--dFzsb').text
    print(f'{star} "{title}"')

# driver.close()
