class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def show_info(self):              
        print(f"Title: {self.title} | Author: {self.author}")

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def download(self):                
        print(f"Downloading {self.title}... Size: {self.file_size}")

class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages
    def read(self):                    
        print(f"Reading {self.title}... Pages: {self.pages}")

e1 = EBook("Python", "John", "50MB")
p1 = PrintedBook("Clean Code", "Robert", 300)

e1.show_info()    
e1.download()   

p1.show_info()    
p1.read()         