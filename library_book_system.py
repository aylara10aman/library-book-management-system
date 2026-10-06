# Base Level

class Book:
    def __init__(self, title, author, isbn, year, genre):
        # Initialize the book attributes
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self.available = True
        self.borrower = None

    def __str__(self):
        # Return a formatted string representation of the book
        return f"{self.isbn:<15} | {self.title:<25} | {self.author:<22} | {self.year:<6} | {self.genre:<12} | {self.get_status()}"

    def check_out(self, borrower_name):
        # Check out the book to a borrower if it is available
        if self.available:
            self.available = False
            self.borrower = borrower_name
            return True
        else:
            return False

    def return_book(self):
        # Return the book and make it available again
        if not self.available:
            self.available = True
            self.borrower = None
            return f"{self.title} has been returned and is now available."
        else:
            return f"{self.title} is already available."

    def get_status(self):
        # Return the current status of the book
        if self.available:
            return "Available"
        else:
            return f"Checked out by {self.borrower}."

book1 = Book("Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925, "Fiction")
book2 = Book("1984", "George Orwell", "9780451524935", 1949, "Dystopian")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960, "Fiction")
book4 = Book("The Hobbit", "J.R.R. Tolkein", "9780544003411", 1937, "Fantasy")
book5 = Book("Pride and Prejudice", "Jane Austen", "9780141439518", 1813, "Romance")
book6 = Book("The Alchemist", "Paulo Coelho", "9780061120084", 1988, "Fiction")

books = [book1, book2, book3, book4, book5, book6]

print("=== Full Collection ===")
for book in books:
    print(book)

if book1.check_out("Lara"):
    print(f"{book1.title} has been checked out by Lara")
else:
    print(f"{book1.title} is already checked out.")

print(book1.get_status())
print(book1.return_book())
print(book1.get_status())

if book2.check_out("John"):
    print(f"{book2.title} has been checked out by John")
else:
    print(f"{book2.title} is already checked out.")

print(book2.get_status())
if book2.check_out("Lara"):
    print(f"{book2.title} has been checked out by Lara")
else:
    print(f"{book2.title} is already checked out.")

sorted_books = sorted(books, key=lambda a: a.title)

print("=== Sorted by Title ===")
for book in sorted_books:
    print(book)

available_books = [book for book in books if book.available]

print("=== Available Books ===")
for book in available_books:
    print(book)

# Testing: the program should represent the full collection, checkout and return results, sorted books, and available books correctly.