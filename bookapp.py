from bookclasses import Book, Category, Publisher

bk1 = Book("Python for All", "Barrid", "Zacky", "Randy", 380)
print(bk1.book_title + bk1.author_first_name + bk1.author_middle_name
      + bk1.author_last_name, bk1.number_of_pages)

bk2 = Category(book_cat="Law")
print(bk2.book_cat)
print(Category.__mro__)