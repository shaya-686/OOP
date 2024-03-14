# До вже реалізованого класу «Автомобіль» додайте
# необхідні перевантажені методи та оператори.

class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages

    def __str__(self):
        return (f"Book information: "
                f"brand - {self.title}, "
                f"model - {self.author},"
                f"genre - {self.genre},"
                f"pages - {self.pages}")

    def __add__(self, page):
        self.pages += page
        return self

    def __sub__(self, page):
        if self.pages < page:
            print("The book has less pages then you provide")
        else:
            self.pages -= page
            return self

    def __eq__(self, other):
        return self.pages == other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __lt__(self, other):
        return self.pages < other.pages


book1 = Book("Harry Potter", "Joanne Rowling", "fantasy", 100)
book2 = Book("Harry Potter", "Joanne Rowling", "fantasy", 100)
print(book1, book2)

print(book1 + 100)
print(book1 - 50)

if book1 == book2:
    print("Books have the same number of pages")
elif book1 > book2:
    print("First book has more pages then the second")
elif book1 < book2:
    print("First book has less pages then the second")
else:
    print("Unknown case")







