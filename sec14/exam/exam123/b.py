from bs4 import BeautifulSoup

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
print(comment)
# <class 'bs4.element.Comment'>