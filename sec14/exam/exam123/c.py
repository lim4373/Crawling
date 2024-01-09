from bs4 import BeautifulSoup

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
# print(comment)
# <class 'bs4.element.Comment'>


coment = []
text_all = []
print(help(soup.recursiveChildGenerator()))