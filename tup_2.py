'''
2. Python Data Structure Challenges in Real-World Scenarios
Task 1: Library System Enhancement
Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement:
You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

Add functionality to insert new books into library.
Ensure that adding a duplicate book is handled appropriately.
'''

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def add_book(library, title, author):
    new_book = (title, author)
    if new_book not in library:
        library.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")
    else:
        print(f"The book '{title}' by {author} already exists in the library.")


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

add_book(library, "To Kill a Mockingbird", "Harper Lee")

add_book(library, "1984", "George Orwell")
