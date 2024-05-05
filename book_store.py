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



