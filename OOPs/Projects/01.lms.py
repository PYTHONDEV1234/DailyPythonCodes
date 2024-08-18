class Book:
    def __init__(self, title , author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f'You have borrowed {self.title}')
        else:
            print("The book is unavailable")
    
    def return_book(self):
        self.available = True
        print("You have returned the book")

class Library:
    def __init__(self):
        self.books=[]

    def add_a_book(self, book):
        self.books.append(book)
        print("Book added successfully.")
    
    def display_books(self):
        if not self.books:
            print("There is no book to display.")
        else:
            print("Listb of books in the library:")
            for book in self.books:
                print(f'Title = {book.title} , author = {book.author}')

    
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
    
    def return_book_to_library(self,title):
        for book in self.books:
            if book.title ==title:
                book.return_book()
    


library= Library()
book1 = Book("The Thirsty Crow","Tim Cook")
book2 = Book("The hungry Bird", "Brad Pitt")
book3 = Book("The friends" , "Chandeler Bing")

print(book1.title)
print(book2.author)
# library.add_a_book(book1)
# library.add_a_book(book2)
# library.add_a_book(book3)
# library.display_books()

# library.borrow_book("The Thirsty Crow")
# # library.borrow_book("The Thirsty Crow")
# library.return_book_to_library("The Thirsty Crow")


    
