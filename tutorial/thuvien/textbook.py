from item import Item

class Textbook(Item):
    def __init__(self, title, author, subject):
        super().__init__(title, author, True)
        self.subject = subject

    def display_info(self):
        print(f"Textbook: {self.title}, Author: {self.author}, Subject: {self.subject}")
