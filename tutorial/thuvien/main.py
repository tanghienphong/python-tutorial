from textbook import Textbook
from novel import Novel

def process_library_item(item):
    item.display_info()
    
print("-----------------Textbook---------------------")
textbook = Textbook("Advanced Python", "John Doe", "Programming")
process_library_item(textbook)

print("-----------------Novel---------------------")
novel = Novel("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
process_library_item(novel)

print("-----------------Borrow and Return (Textbook)---------------------")
textbook.borrow()
process_library_item(textbook)
textbook.return_item()

print("-----------------Borrow and Return (Novel)---------------------")
novel.borrow()
process_library_item(novel)
novel.return_item()