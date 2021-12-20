import sys
import os
import time
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




path ="C:\\Users\\emman\\Documents\\To Anki"
directory= os.listdir(path) 


def check_for_new_decks():
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


def move_converted_decks_to_exportedfolder():
    print("In Move converted item to exported folder")

    for item in directory:
        if item == "Exported":  
            print("This is the 'Exported' folder, NO TRESPASSING ")
            pass
        else:
            print(f"We are moving {item}")
            source = f"C:\\Users\\emman\\Documents\\To Anki\\{item}"
            destination = f"C:\\Users\\emman\\Documents\\To Anki\\Exported\\Pediatrics\\{item}"
            shutil.move(source,destination)

            print(f"{item} has been moved from {source} to {destination} .")

    
def convert_notion_to_anki():
    # using web scraping 

    # Go to the web page and edit the options to enable avocado and some

    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/a').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[2]/section/div/div[2]/div/label[6]').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/button[1]').click()
    file_input = driver.find_element(By.NAME, "pakker")

    #loop throug the items to be uploaded, excluding the "Exported folder", upload them to the site
    for item in directory:
        print(item)
        if item == "Exported":  
            print("This is the 'Exported' folder, NO TRESPASSING ")
            pass
        else:
            print("This is a not the 'Exported' folder, Carry on")
            print("The path is", f"C:\\Users\\emman\\Documents\\To Anki\\{item}")
            print(f"C:\\Users\\emman\\Documents\\To Anki\\{item}")
            file_input.send_keys(f"C:\\Users\\emman\\Documents\\To Anki\\{item}")

        
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > div.container > form > div > div > a").click()

    print("Downloaded")
    time.sleep(5)
    driver.close()

# print(check_for_new_decks())

if check_for_new_decks() == "Empty":
    print("No new decks")
else:

    driver = webdriver.Chrome(executable_path='C:/Users/emman/Desktop/stuff/chromedriver_win32/chromedriver.exe')
    driver.get("https://2anki.net/upload")
    driver.maximize_window()

    convert_notion_to_anki()
    print("Converted")

    move_converted_decks_to_exportedfolder()
    print("Moved")
