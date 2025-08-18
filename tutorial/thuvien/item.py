from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self._available = available

    @abstractmethod
    def display_info(self):
        pass
    
    def borrow(self):
        if self._available:
            self._available = False
            print(f"You have borrowed the textbook: {self.title}")
        else:
            print(f"Sorry, the textbook: {self.title} is not available for borrowing.")

    def return_item(self):
        self._available = True
        print(f"You have returned the textbook: {self.title}")
