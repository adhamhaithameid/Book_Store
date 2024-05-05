class Item:
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self._price = price

    def update_details(self, title=None, author=None, price=None):
        if title is not None:
            self._title = title
        if author is not None:
            self._author = author
        if price is not None:
            self._price = price

    def __str__(self):
        return f"{self._title} by {self._author}, ${self._price:.2f}"



class Book(Item):
    def __init__(self, title, author, price, ISBN, genre, number_of_pages):
        super().__init__(title, author, price)
        self._ISBN = ISBN
        self._genre = genre
        self._number_of_pages = number_of_pages

    def update_details(self, ISBN=None, genre=None, number_of_pages=None, **kwargs):
        super().update_details(**kwargs)
        if ISBN is not None:
            self._ISBN = ISBN
        if genre is not None:
            self._genre = genre
        if number_of_pages is not None:
            self._number_of_pages = number_of_pages

    def __str__(self):
        return f"{super().__str__()}, ISBN: {self._ISBN}, {self._genre}, {self._number_of_pages} pages"



class Magazine(Item):
    def __init__(self, title, author, price, issue_number, publication_date, editor):
        super().__init__(title, author, price)
        self._issue_number = issue_number
        self._publication_date = publication_date
        self._editor = editor

    def update_details(self, issue_number=None, publication_date=None, editor=None, **kwargs):
        super().update_details(**kwargs)
        if issue_number is not None:
            self._issue_number = issue_number
        if publication_date is not None:
            self._publication_date = publication_date
        if editor is not None:
            self._editor = editor

    def __str__(self):
        return f"{super().__str__()}, Issue {self._issue_number}, {self._publication_date}, Editor: {self._editor}"



class DVD(Item):
    def __init__(self, title, author, price, director, duration, genre):
        super().__init__(title, author, price)
        self._director = director
        self._duration = duration
        self._genre = genre

    def update_details(self, director=None, duration=None, genre=None, **kwargs):
        super().update_details(**kwargs)
        if director is not None:
            self._director = director
        if duration is not None:
            self._duration = duration
        if genre is not None:
            self._genre = genre

    def __str__(self):
        return f"{super().__str__()}, Directed by {self._director}, {self._duration} min, {self._genre}"



class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def search_item(self, search_query):
        results = []
        for item in self.items:
            if search_query.lower() in item._title.lower() or search_query.lower() in item._author.lower():
                results.append(item)
        return results

    def list_inventory(self):
        for item in self.items:
            print(item)

    def __str__(self):
        return "\n".join(str(item) for item in self.items)



def add_item_to_inventory(inventory):
    print("Add a new item to the inventory.")
    item_type = input("Enter item type (book/magazine/dvd): ").lower()
    title = input("Enter title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))
    
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

    inventory.add_item(item)
    print("Item added successfully!")

def search_inventory(inventory):
    query = input("Enter search query (title or author): ")
    results = inventory.search_item(query)
    if results:
        print("Search Results:")
        for result in results:
            print(result)
    else:
        print("No items found.")



