class LibraryBook:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False


class LibraryBookExtended(LibraryBook):
    def __init__(self, title, author, publication_year, condition):
        super().__init__(title, author, publication_year)
        self.condition = condition

    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}, Condition: {self.condition}"


# Використання
book = LibraryBookExtended("1984", "George Orwell", 1949, "Good")
print(book.check_out())
print(book.check_out())
print(book.get_book_info())