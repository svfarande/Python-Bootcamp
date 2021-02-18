class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # overriding inbuilt str method
        return f"{self.title} by {self.author}"

    def __len__(self):  # overriding inbuilt len method
        return self.pages

    def __del__(self):  # overriding inbuilt del method
        print("Book - " + self.title + " deleted")


b = Book("P for Python", "Shubham", 50)

print(b)
print(str(b))
print(len(b))
del b
