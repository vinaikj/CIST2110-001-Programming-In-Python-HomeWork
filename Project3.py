#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|
# Author: Jayant Vinaik
# CIST2110-001-Project-3 Library Management System (LMS)
# Project 3 will implement a library management system (LMS) that will allow users to manage books, users, and a library to manage collection of books and users.
# The LMS will be menu driven and will allow users to add, delete, and update books and users.
# Users will also be able to borrow and return books.
# The LMS will also allow users to search for books and users.

# ENABLE WORD WRAP TO MAKE THINGS EASIER TO READ:
# VIEW (at the top) -> WORD WRAP

# Import statements:
import csv
# Project outline and requirements:


class Book:
  def __init__(self, title, author, isbn):
      self.isbn = isbn
      self.title = title
      self.author = author
      self.borrowed = False

  def __str__(self):
    return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Borrowed: {self.borrowed}"

  def check_out(self):
    self.borrowed = True
    return f"Book '{self.title}' checked out."

  def check_in(self):
    self.borrowed = False
    return f"Book '{self.title}' checked in."

  def is_borrowed(self):
    return self.borrowed

class User:
  def __init__(self, name, member_id):
      self.name = name
      self.member_id = member_id
      self.borrowed_books = []

  def __str__(self):
    borrowed_books_titles = [book.title for book in self.borrowed_books]
    return f"Name: {self.name}, ID: {self.user_id}, Borrowed Books: {', '.join(borrowed_books_titles)}"

  def borrow_book(self, book):
    self.borrowed_books.append(book)
    book.check_out()
    return f"Book '{book.title}' borrowed by {self.name}."

  def return_book(self, book):
    if book in self.borrowed_books:
        self.borrowed_books.remove(book)
        book.check_in()
        return f"Book '{book.title}' returned by {self.name}."
    else:
        return f"Book '{book.title}' not found in borrowed books for {self.name}."

class Library:
  def __init__(self):
      self.books = []
      self.users = []

  def __str__(self):
    return f"Books: {len(self.books)}, Users: {len(self.users)}"

  def add_book(self, book):
    self.books.append(book)
    return f"Book '{book.title}' added to the library."

  def add_user(self, user):
    self.users.append(user)
    return f"User '{user.name}' added to the library."

  def find_book(self, isbn):
    for book in self.books:
        if book.isbn == isbn:
            return book
    return None

  def find_user(self, user_id):
    for user in self.users:
        if user.member_id == user_id:
            return user
    return None

  def export_books_to_csv(self, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ISBN', 'Title', 'Author', 'Borrowed'])
        writer.writeheader()
        for book in self.books:
            writer.writerow({'ISBN': book.isbn, 'Title': book.title, 'Author': book.author, 'Borrowed': book.borrowed})

  def export_users_to_csv(self, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'ID', 'Borrowed Books'])
        writer.writeheader()
        for user in self.users:
            borrowed_books_titles = [book.title for book in user.borrowed_books]
            writer.writerow({'Name': user.name, 'ID': user.user_id, 'Borrowed Books': ', '.join(borrowed_books_titles)})

def print_menu():
  print("Library Management System Menu:")
  print("1. Add Book")
  print("2. Add User")
  print("3. Delete Book")
  print("4. Delete User")
  print("5. Borrow Book")
  print("6. Return Book")
  print("7. Search Books")
  print("8. Check Book Availability")
  print("9. Search Users")
  print("10. Export Books to CSV")
  print("11. Export Users to CSV")
  print("12. Exit")

def main():
  library = Library()

  while True:
      print_menu()
      choice = input("Enter your choice: ")

      if choice == '1':
          isbn = int(input("Enter ISBN: "))
          title = input("Enter Title: ")
          author = input("Enter Author: ")
          book = Book(isbn, title, author)
          print(library.add_book(book))

      elif choice == '2':
          name = input("Enter Name: ")
          user_id = int(input("Enter User ID: "))
          user = User(name, user_id)
          print(library.add_user(user))

      elif choice == '3':
          isbn = int(input("Enter ISBN of the book to delete: "))
          book = library.find_book(isbn)
          if book:
              library.books.remove(book)
              print(f"Book '{book.title}' deleted from the library.")
          else:
              print(f"Book with ISBN {isbn} not found in the library.")

      elif choice == '4':
          user_id = int(input("Enter User ID of the user to delete: "))
          user = library.find_user(user_id)
          if user:
              library.users.remove(user)
              print(f"User '{user.name}' deleted from the library.")
          else:
              print(f"User with ID {user_id} not found in the library.")

      elif choice == '5':
          isbn = int(input("Enter ISBN of the book to borrow: "))
          book = library.find_book(isbn)
          if book:
              user_id = int(input("Enter User ID to borrow the book: "))
              user = library.find_user(user_id)
              if user:
                  print(user.borrow_book(book))
              else:
                  print(f"User with ID {user_id} not found in the library.")
          else:
              print(f"Book with ISBN {isbn} not found in the library.")

      elif choice == '6':
          isbn = int(input("Enter ISBN of the book to return: "))
          book = library.find_book(isbn)
          if book:
              user_id = int(input("Enter User ID to return the book: "))
              user = library.find_user(user_id)
              if user:
                  print(user.return_book(book))
              else:
                  print(f"User with ID {user_id} not found in the library.")
          else:
              print(f"Book with ISBN {isbn} not found in the library.")

      elif choice == '7':
        search_term = input("Enter the search term for books: ")
        results = library.find_book(search_term)
        if results:
          print("Search results for books:")
          for book in results:
              print(book)
        else:
          print("No books found matching the search term.")

      elif choice == '8':
          isbn = int(input("Enter ISBN of the book to check availability: "))
          book = library.find_book(isbn)
          if book:
              if book.is_borrowed():
                  print(f"Book '{book.title}' is currently borrowed.")
              else:
                  print(f"Book '{book.title}' is available.")
          else:
              print(f"Book with ISBN {isbn} not found in the library.")

      elif choice == '9':
        search_term = input("Enter the search term for users: ")
        results = library.find_user(search_term)
        if results:
          print("Search results for users:")
          for user in results:
              print(user)
        else:
          print("No users found matching the search term.")

      elif choice == '10':
          filename = input("Enter the filename to export books to CSV: ")
          library.export_books_to_csv(filename)
          print(f"Books exported to {filename}.")

      elif choice == '11':
          filename = input("Enter the filename to export users to CSV: ")
          library.export_users_to_csv(filename)
          print(f"Users exported to {filename}.")

      elif choice == '12':
          print("Exiting the Library Management System. Goodbye!")
          break

      else:
          print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()