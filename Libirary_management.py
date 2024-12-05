import datetime

class Library:
    def __init__(self):
        self.books = {}  # Format: {ISBN: {"title": str, "author": str, "available": bool, "borrowed_by": str}}
        self.members = {}  # Format: {member_id: {"name": str, "books_borrowed": list}}
        self.borrow_history = []  # Format: [{"ISBN": str, "member_id": str, "borrow_date": date, "return_date": date}]

    def add_book(self, ISBN, title, author):
        if ISBN in self.books:
            print("Book already exists!")
        else:
            self.books[ISBN] = {"title": title, "author": author, "available": True, "borrowed_by": None}
            print(f"Book '{title}' added successfully!")

    def register_member(self, member_id, name):
        if member_id in self.members:
            print("Member already registered!")
        else:
            self.members[member_id] = {"name": name, "books_borrowed": []}
            print(f"Member '{name}' registered successfully!")

    def borrow_book(self, ISBN, member_id):
        if ISBN not in self.books:
            print("Book not found!")
            return
        if not self.books[ISBN]["available"]:
            print("Book is already borrowed!")
            return
        if len(self.members[member_id]["books_borrowed"]) >= 3:
            print("Member cannot borrow more than 3 books!")
            return

        self.books[ISBN]["available"] = False
        self.books[ISBN]["borrowed_by"] = member_id
        self.members[member_id]["books_borrowed"].append(ISBN)
        self.borrow_history.append({"ISBN": ISBN, "member_id": member_id, "borrow_date": datetime.date.today(), "return_date": None})
        print(f"Book '{self.books[ISBN]['title']}' borrowed successfully!")

    def return_book(self, ISBN, member_id):
        if ISBN not in self.members[member_id]["books_borrowed"]:
            print("Member has not borrowed this book!")
            return

        self.books[ISBN]["available"] = True
        self.books[ISBN]["borrowed_by"] = None
        self.members[member_id]["books_borrowed"].remove(ISBN)

        for record in self.borrow_history:
            if record["ISBN"] == ISBN and record["member_id"] == member_id and record["return_date"] is None:
                record["return_date"] = datetime.date.today()
                break

        print(f"Book '{self.books[ISBN]['title']}' returned successfully!")

    def display_books(self):
        print("\nAvailable Books:")
        for ISBN, info in self.books.items():
            if info["available"]:
                print(f"ISBN: {ISBN}, Title: {info['title']}, Author: {info['author']}")

    def member_history(self, member_id):
        print(f"\nBorrow History for Member '{self.members[member_id]['name']}':")
        for record in self.borrow_history:
            if record["member_id"] == member_id:
                print(f"ISBN: {record['ISBN']}, Borrow Date: {record['borrow_date']}, Return Date: {record['return_date']}")

    def most_borrowed_books(self):
        count = {}
        for record in self.borrow_history:
            ISBN = record["ISBN"]
            count[ISBN] = count.get(ISBN, 0) + 1
        sorted_books = sorted(count.items(), key=lambda x: x[1], reverse=True)
        print("\nMost Borrowed Books:")
        for ISBN, borrow_count in sorted_books[:5]:
            print(f"ISBN: {ISBN}, Title: {self.books[ISBN]['title']}, Borrowed: {borrow_count} times")

    def overdue_books(self):
        today = datetime.date.today()
        overdue_days = 7
        print("\nOverdue Books:")
        for record in self.borrow_history:
            if record["return_date"] is None and (today - record["borrow_date"]).days > overdue_days:
                print(f"ISBN: {record['ISBN']}, Borrowed By: {record['member_id']}, Borrowed Date: {record['borrow_date']}")

    def save_data_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(str(self.books) + "\n")
            file.write(str(self.members) + "\n")
            file.write(str(self.borrow_history) + "\n")
        print("Library data saved successfully!")

    def load_data_from_file(self, filename):
        with open(filename, "r") as file:
            data = file.readlines()
            self.books = eval(data[0])  # Potentially unsafe
            self.members = eval(data[1])
            self.borrow_history = eval(data[2])
        print("Library data loaded successfully!")

# Main program to test the system
def main():
    library = Library()
    while True:
        print("\n--- Library Management Menu ---")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Member Borrow History")
        print("7. Most Borrowed Books")
        print("8. Overdue Books")
        print("9. Save Library Data")
        print("10. Load Library Data")
        print("11. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                ISBN = input("Enter ISBN: ")
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                library.add_book(ISBN, title, author)
            elif choice == 2:
                member_id = input("Enter Member ID: ")
                name = input("Enter Member Name: ")
                library.register_member(member_id, name)
            elif choice == 3:
                ISBN = input("Enter ISBN to borrow: ")
                member_id = input("Enter Member ID: ")
                library.borrow_book(ISBN, member_id)
            elif choice == 4:
                ISBN = input("Enter ISBN to return: ")
                member_id = input("Enter Member ID: ")
                library.return_book(ISBN, member_id)
            elif choice == 5:
                library.display_books()
            elif choice == 6:
                member_id = input("Enter Member ID: ")
                library.member_history(member_id)
            elif choice == 7:
                library.most_borrowed_books()
            elif choice == 8:
                library.overdue_books()
            elif choice == 9:
                filename = input("Enter filename to save data: ")
                library.save_data_to_file(filename)
            elif choice == 10:
                filename = input("Enter filename to load data: ")
                library.load_data_from_file(filename)
            elif choice == 11:
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
