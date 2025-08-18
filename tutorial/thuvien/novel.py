from item import Item

class Novel(Item):
    def __init__(self, title, author, genre):
        super().__init__(title, author, True)
        self.genre = genre

    def display_info(self):
        print(f"Novel: {self.title}, Author: {self.author}, Genre: {self.genre}")

        
