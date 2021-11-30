class Book(object):
    def __init__(self, book_title, author_first_name, author_middle_name, author_last_name, number_of_pages):
        self.book_title = book_title,
        self.author_first_name = author_first_name,
        self.author_middle_name = author_middle_name,
        self.author_last_name = author_last_name,
        self.number_of_pages = number_of_pages
        
        super(Book, self).__init__()


class Category(Book):
    def __init__(self, book_cat):
        self.book_cat = book_cat
        print("My category class")
        super(Category, self).__init__()


class Publisher(Book, Category):
    def __init__(self, publisher_name, publisher_location):
        self.publisher_name = publisher_name
        self.publisher_location = publisher_location
        super(Publisher, self).__init__()

    def printRun(self):
        pass
