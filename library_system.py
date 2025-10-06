class Book:
    def __init__(self,title,author,availabe = True):
        self.title = title
        self.author = author
        self.availabe = availabe

class Library:
    def __init__(self):
        self.books = []
        
