class Book:
    ####생성자 ##코드추가
    def __init__(self, title, author):


    def check_out(self):
        self.is_checked_out = True

    def check_in(self):
        ##코드추가

    #추가 __str__

##  pyreverse -o png  classview/Score.py

class Library:
    def __init__(self):
        self.books = []

    ##########각 메소드 내용 추가.
    def add_book(self, book):


    def remove_book(self, title):


    def find_by_author(self, author):


    def find_by_title(self, title):


    def is_available(self, title):
        for book in self.books:
            if book.title == title:
                return not book.is_checked_out
        return False

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.check_out()
                return

    def check_in_book(self, title):
        for book in self.books:
            if book.title == title and book.is_checked_out:
                book.check_in()
                return

    ####__str __ or  __repr__추가




if __name__ == "__main__":
    library = Library()
    book1 = Book("위대한 개츠비", "F. 스콧 피츠제럴드")
    book2 = Book("1984", "조지 오웰")

    library.add_book(book1)
    library.add_book(book2)

    book_to_checkout = "위대한 개츠비"
    if library.is_available(book_to_checkout):
        library.check_out_book(book_to_checkout)
        print(f"'{book_to_checkout}'을(를) 대출하였습니다.")
    else:
        print(f"'{book_to_checkout}'은(는) 대출 가능한 상태가 아닙니다.")

    print("\n도서관 현황:")
    print(library)

    library.check_in_book(book_to_checkout)
    print(f"\n'{book_to_checkout}'을(를) 반납하였습니다.")


    print("\n도서관 현황:")
    print(library)
