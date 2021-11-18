import sys
import os



# print(f"The current working directory is {os.getcwd()}")
# os.chdir("C:\\Users\\emman\\Projects\\notion_anki_auto")
# print(f"The current working directory is {os.getcwd()}")

# path ="C:\\Users\\emman\\Projects\\notion_anki_auto" 

def check_for_new_decks():
    path ="C:\\Users\\emman\\Documents\\To Anki"
    directory= os.listdir(path) 
    if len(directory) == 1: 
        print(f"The number of items in the directory is {len(directory)}")
        print(directory)
        print("The folder is empty \nThere are no new decks") 
        return "Empty"
    else: 
        print(f"The number of items in the directory is {len(directory)}")
        print(directory)
        print("There is more than one item in the folder \nThere are new decks")
        return "Not Empty"
    
print(check_for_new_decks())