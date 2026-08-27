""" - Library tracking system -
A dictionary to track each book's status: Borrow book, check system, available, days"""
import csv

class LibraryTracking():
  def __init__(self, file_path):
    self.file_path = file_path
    self.books = {}
    self.load_books()

  def load_books(self):
    with open(self.file_path, "r") as file:
      reader = csv.DictReader(file)
      for row in reader:
        self.books[row["book_name"]] = row["status"]
    
  def search_book(self, book_name):
    if book_name in self.books:
      status = self.books[book_name]
      print(f" '{book_name}' is {status}")
    else:
      print(f" '{book_name}' not found in library system.")

  def borrow_book(self, book_name):
    if book_name not in self.books:
      print(f" '{book_name}' not found in library system.")
    elif self.books[book_name] == "borrowed":
      print(f" '{book_name}' is not available. Someone is already borrow the book.")
    elif self.books[book_name] == "available":
      self.books[book_name] = "borrowed"
      self.save_books()
      print(f" Successfully borrowed '{book_name}' for 7 days. Please renew if you need more time")

  def save_book(self, book_name):
    writer.writerow([book_name, status])
    for book, status in self.books.items():
      writer.writerow([book, status])

  def return_book(self, book_name):
    if book_name not in self.books:
      print(f" '{book_name}' not found in library system.)
    elif self.books[book_name] == "available":
      print(f" '{book_name}' is not borrowed")
    else:
      
        
    
library = LibraryTracking("d:\\Dump\\books.csv")

while True:
  print("\n=== Library Tracking ===")
  print("1. Search book")
  print("2. Borrow book")
  print("3. Return book")
  print("4. Show all book")
  print("5. Quit")
  choice = input("Choose option: ")

  if choice == "1":
    name = input("Enter your book name")
    library.search_book(name)
  elif choice == "2":
    name = input("Enter book name to borrow: ")
    library.borrow_book(book_name)
  elif choice == "3":
    name = input("Enter book name to return: ")
    library.return_book(book_name)
  elif choice == "4":
    library.showallbooks()
  elif choice == "5":
    return none
  else:
    print(f" You enter invalid number")


