class User(object):
    
    """The Init method is a special method that runs automaticallywhenever
    a new instance is created based on this class"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("This user’s email has been updated to " + self.email)

    def __repr__(self):
        return "User " + self.name + ', email: ' + self.email + ", books read: " + str(len(self.books))

    def __eq__(self, other_user):
        """A User object should be equal to another User object if they both have the same name and email."""
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating = "None"):
        self.books[book] = rating

    def get_average_rating(self):
        total_user_rating = 0
        count_user_rating = len(self.books)
        
        for value in self.books.values():
            total_user_rating += value
        
        average_user_rating = total_user_rating / count_user_rating
        
        return average_user_rating

#create a book

class Book(object):

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("this book’s ISBN has been updated")

    def add_rating(self, rating):
        if int(rating) >= 0 and int(rating) <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
        
    def __eq__(self,other_book):
        self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        total_book_rating = 0
        count_book_rating = len(self.ratings)
        
        for value in self.ratings:
            total_book_rating += value

        average_book_rating = total_book_rating / count_book_rating
        return average_book_rating

    def __hash__(self):
        return hash((self.title, self.isbn))
            
#Make a Fiction Subclass of Book

class Fiction(Book):

    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return title + ' by ' + self.author
        
#Make a Non-Fiction Subclass of Book

class Non_Fiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return title + ', a ' + level + ' manual on ' + self.subject

#TomeRater

class TomeRater(object):

    def __init__(self):
        self.users = {  }
        self.books = {}
        
    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        fiction = Fiction(title, author, isbn)
        return fiction

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating = "None"):
        if email not in self.users.key():
            print("No user with email " + email + "!")
        else:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1

    def add_user(self, name, email, books = None):
        user = User(name, email)
        if books != None:
            for book in books:
                self.add_book_to_user(book, email)

#Analysis Methods

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_read = 0
        most_read_book = None

        for key, value in self.books:
            if key > most_read:
                most_read = key
                most_read_book = book
        return book

    def highest_rated_book(self):
        highest_rating = 0
        highest_rating_book = None
        
        for book in self.books.keys():
            if book.get_average_rating() > high_rating:
                highest_rating = book.get_average_rating()
                highest_rating_book = book
        return highest_rating_book
            
    def most_positive_user(self):
        highest_average_rating = 0
        highest_average_rating_user = None
        
        for user in self.users.values():
            if user.get_average_rating() > highest_average_rating:
                highest_average_rating = user.get_average_rating()
                highest_average_rating_user = user
        return highest_average_rating_user
                
            

            
    
    
