# Define a base class for all items in the bookstore
class Item:
    def __init__(self, title, author, price):
        self.title = title  # Title of the item
        self.author = author  # Author of the item
        self.price = price  # Price of the item

    # Update the details of the item
    def update_details(self, title=None, author=None, price=None):
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if price is not None:
            self.price = price

    # Return a string representation of the item
    def __str__(self):
        return f"{self.title} by {self.author}, ${self.price:.2f}"

# Define a class for books, inheriting from Item
class Book(Item):
    def __init__(self, title, author, price, ISBN, genre, number_of_pages):
        super().__init__(title, author, price)
        self.ISBN = ISBN  # ISBN number of the book
        self.genre = genre  # Genre of the book
        self.number_of_pages = number_of_pages  # Number of pages in the book

    # Update details specific to books
    def update_details(self, ISBN=None, genre=None, number_of_pages=None, **kwargs):
        super().update_details(**kwargs)
        if ISBN is not None:
            self.ISBN = ISBN
        if genre is not None:
            self.genre = genre
        if number_of_pages is not None:
            self.number_of_pages = number_of_pages

    # Return a string representation of the book
    def __str__(self):
        return f"{super().__str__()}, ISBN: {self.ISBN}, Genre: {self.genre}, Pages: {self.number_of_pages}"

# Define a class for magazines, inheriting from Item
class Magazine(Item):
    def __init__(self, title, author, price, issue_number, publication_date, editor):
        super().__init__(title, author, price)
        self.issue_number = issue_number  # Issue number of the magazine
        self.publication_date = publication_date  # Publication date of the magazine
        self.editor = editor  # Editor of the magazine

    # Update details specific to magazines
    def update_details(self, issue_number=None, publication_date=None, editor=None, **kwargs):
        super().update_details(**kwargs)
        if issue_number is not None:
            self.issue_number = issue_number
        if publication_date is not None:
            self.publication_date = publication_date
        if editor is not None:
            self.editor = editor

    # Return a string representation of the magazine
    def __str__(self):
        return f"{super().__str__()}, Issue {self.issue_number}, Date: {self.publication_date}, Editor: {self.editor}"

# Define a class for DVDs, inheriting from Item
class DVD(Item):
    def __init__(self, title, author, price, director, duration, genre):
        super().__init__(title, author, price)
        self.director = director  # Director of the DVD
        self.duration = duration  # Duration of the DVD in minutes
        self.genre = genre  # Genre of the DVD

    # Update details specific to DVDs
    def update_details(self, director=None, duration=None, genre=None, **kwargs):
        super().update_details(**kwargs)
        if director is not None:
            self.director = director
        if duration is not None:
            self.duration = duration
        if genre is not None:
            self.genre = genre

    # Return a string representation of the DVD
    def __str__(self):
        return f"{super().__str__()}, Directed by {self.director}, {self.duration} min, Genre: {self.genre}"

# Define a class to manage the orders of items
class Order:
    def __init__(self):
        self.items = []
        self.status = "open"  # Order status could be 'open', 'paid', 'shipped', etc.

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def total_cost(self):
        return sum(item.price * quantity for item, quantity in self.items)

    def complete_order(self):
        self.status = "paid"

    def __str__(self):
        items_str = "\n".join([f"{item.title} (x{quantity}) - ${item.price}" for item, quantity in self.items])
        return f"Order Details:\n{items_str}\nTotal Cost: ${self.total_cost():.2f}"

# Define a class to manage the sales
class SalesManager:
    def __init__(self):
        self.orders = []  # List to hold completed orders
        self.total_sales = 0.0  # Total sales amount

    def add_order(self, order):
        if order.status == "paid":
            self.orders.append(order)
            self.total_sales += order.total_cost()  # Ensure total sales are accumulated

    def get_total_sales(self):
        return self.total_sales

    def get_sales_report(self):
        report = f"Total Sales: ${self.get_total_sales():.2f}\n\nDetailed Orders:\n"
        for order in self.orders:
            report += f"{order}\n"
        return report


# Define a class to manage the inventory of items
class Inventory:
    def __init__(self):
        self.items = []  # List to store items

    # Add an item to the inventory
    def add_item(self, item):
        self.items.append(item)

    # Remove an item from the inventory
    def remove_item(self, item):
        self.items.remove(item)

    # Search for items in the inventory
    def search_item(self, search_query):
        results = []
        for item in self.items:
            if search_query.lower() in item.title.lower() or search_query.lower() in item.author.lower():
                results.append(item)
        return results

    # Print all items in the inventory
    def list_inventory(self):
        for item in self.items:
            print(item)

    # Return a string representation of all items in the inventory
    def __str__(self):
        return "\n".join(str(item) for item in self.items)

# Function to handle adding items to the inventory
def add_item_to_inventory(inventory):
    print("Add a new item to the inventory.")
    item_type = input("Enter item type (book/magazine/dvd): ").lower()

    # Collect common item details with basic validation
    try:
        title = input("Enter title: ")
        author = input("Enter author: ")
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid input for price. Please enter a valid number.")
        return

    # Handle specific types of items
    try:
        if item_type == 'book':
            ISBN = input("Enter ISBN: ")
            genre = input("Enter genre: ")
            number_of_pages = int(input("Enter number of pages: "))
            item = Book(title, author, price, ISBN, genre, number_of_pages)
        elif item_type == 'magazine':
            issue_number = input("Enter issue number: ")
            publication_date = input("Enter publication date: ")
            editor = input("Enter editor: ")
            item = Magazine(title, author, price, issue_number, publication_date, editor)
        elif item_type == 'dvd':
            director = input("Enter director: ")
            duration = int(input("Enter duration (in minutes): "))
            genre = input("Enter genre: ")
            item = DVD(title, author, price, director, duration, genre)
        else:
            print("Invalid item type entered.")
            return
    except ValueError:
        print("Invalid numerical input where a number was expected. Please try again.")
        return

    inventory.add_item(item)
    print("Item added successfully!")

# Function to create an order in the inventory
def create_order(inventory):
    order = Order()
    print("\n=================================================================")
    print("Create a New Order")
    print("=================================================================")
    while True:
        # Let user select the item type first
        print("\nAvailable item types: Book, Magazine, DVD")
        item_type = input("Enter the type of item you want to order or 'done' to finish: ").strip().lower()
        if item_type == 'done':
            if not order.items:
                print("No items were added to the order. Cancelling order.")
                return None
            break

        if item_type not in ['book', 'magazine', 'dvd']:
            print("Invalid item type. Please choose from 'book', 'magazine', or 'dvd'.")
            continue

        item_title = input(f"Enter the title of the {item_type} to add to the order: ").strip()
        # Search for items by title and type
        found_items = [item for item in inventory.search_item(item_title) if isinstance(item, {'book': Book, 'magazine': Magazine, 'dvd': DVD}[item_type])]
        if not found_items:
            print("No matching items found in inventory. Please try another title or type.")
            continue

        # Display found items and let user select
        for idx, item in enumerate(found_items, 1):
            print(f"{idx}. {item}")
        item_index = safe_input("number of the item you want to add", int) - 1
        if item_index not in range(len(found_items)):
            print("Invalid selection. Please enter a valid number from the list.")
            continue

        quantity = safe_input("quantity for this item", int)
        order.add_item(found_items[item_index], quantity)
        print(f"Added {quantity} of {found_items[item_index].title} ({item_type}) to the order.")

    if order.items:
        print("\nFinalizing Order...")
        print(order)
        order.complete_order()
        return order
    else:
        print("No items added to the order.")
        return None

# Function to search for items in the inventory
def search_inventory(inventory):
    query = input("Enter search query (title or author): ")
    results = inventory.search_item(query)
    if results:
        print("Search Results:")
        for result in results:
            print(result)
    else:
        print("No items found.")

# Main function to drive the program
def main():
    inventory = Inventory()
    sales_manager = SalesManager()

    while True:
        print("\n=================================================================")
        print("Welcome to the Online Bookstore Management System!")
        print("=================================================================")
        print("1. Add Item to Inventory")
        print("2. Search for Items")
        print("3. Display Inventory")
        print("4. Place an Order")
        print("5. View Sales Report")
        print("6. Exit")
        print("=================================================================")
        choice = input("Please choose an option (1-6): ")

        if choice == '1':
            add_item_to_inventory(inventory)
        elif choice == '2':
            search_inventory(inventory)
        elif choice == '3':
            print("\nCurrent Inventory:")
            inventory.list_inventory()
        elif choice == '4':
            order = create_order(inventory)
            if order:
                sales_manager.add_order(order)
                print("\nOrder completed and added to sales.")
        elif choice == '5':
            print("\nSales Report:")
            print(sales_manager.get_sales_report())
        elif choice == '6':
            print("\nThank you for using our system. Goodbye!")
            break
        else:
            print("\nInvalid option. Please enter a number between 1 and 6.")

def add_item_to_inventory(inventory):
    print("\n=================================================================")
    print("Add a New Item to Inventory")
    print("=================================================================")
    item_type = input("Enter item type (book/magazine/dvd): ").strip().lower()
    if item_type not in ['book', 'magazine', 'dvd']:
        print("Invalid item type entered. Please choose from 'book', 'magazine', or 'dvd'.")
        return
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    try:
        price = float(input("Enter price (numeric value): "))
    except ValueError:
        print("Invalid price entered. Please enter a valid numeric value.")
        return
    
    if item_type == 'book':
        ISBN = input("Enter ISBN: ").strip()
        genre = input("Enter genre: ").strip()
        number_of_pages = safe_input("number of pages", int)
        item = Book(title, author, price, ISBN, genre, number_of_pages)
    elif item_type == 'magazine':
        issue_number = safe_input("issue number", int)
        publication_date = input("Enter publication date (e.g., 2024-05-01): ").strip()
        editor = input("Enter editor: ").strip()
        item = Magazine(title, author, price, issue_number, publication_date, editor)
    elif item_type == 'dvd':
        director = input("Enter director: ").strip()
        duration = safe_input("duration (in minutes)", int)
        genre = input("Enter genre: ").strip()
        item = DVD(title, author, price, director, duration, genre)

    inventory.add_item(item)
    print("Item successfully added to inventory.")

def safe_input(prompt, type_func):
    while True:
        try:
            return type_func(input(f"Enter {prompt}: "))
        except ValueError:
            print(f"Invalid input. Please enter a valid {type(prompt).__name__}.")

if __name__ == "__main__":
    main()
