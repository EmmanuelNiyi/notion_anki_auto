import sys
import os



print(f"The current working directory is {os.getcwd()}")
os.chdir("C:\\Users\\emman\\Projects\\notion_anki_auto")
print(f"The current working directory is {os.getcwd()}")

# path ="C:\\Users\\emman\\Projects\\notion_anki_auto" 
path ="C:\\Users\\emman\\Documents\\To Anki"
directory= os.listdir(path) 
if len(directory) == 0: 
    
    print("Empty directory") 
else: 
    print("Not empty directory")
    print(directory)
    print(f"The number of items in the directory is {len(directory)}")