# bookstore.py

class Bookstore:
    def __init__(self):
        self.books = {}

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        publisher = input("Enter book publisher: ")
        self.books[title] = {"author": author, "publisher": publisher}
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter book title: ")
        if title in self.books:
            del self.books[title]
            print("Book removed successfully!")
        else:
            print("Book not found!")

    def update_book(self):
        title = input("Enter book title: ")
        if title in self.books:
            author = input("Enter new author: ")
            publisher = input("Enter new publisher: ")
            self.books[title] = {"author": author, "publisher": publisher}
            print("Book updated successfully!")
        else:
            print("Book not found!")

    def get_all_books(self):
        if not self.books:
            print("No books available!")
        else:
            for title, info in self.books.items():
                print(f"Title: {title}, Author: {info['author']}, Publisher: {info['publisher']}")

    def get_books_by_author(self):
        author = input("Enter author name: ")
        found = False
        for title, info in self.books.items():
            if info["author"] == author:
                print(f"Title: {title}, Author: {info['author']}, Publisher: {info['publisher']}")
                found = True
        if not found:
            print("No books found by this author!")

    def run(self):
        while True:
            print("\nBookstore Management System")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Update a book")
            print("4. List all books")
            print("5. Search books by author")
            print("6. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.update_book()
            elif choice == "4":
                self.get_all_books()
            elif choice == "5":
                self.get_books_by_author()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again!")

if __name__ == "__main__":
    bookstore = Bookstore()
    bookstore.run()