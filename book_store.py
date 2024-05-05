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



