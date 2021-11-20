import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge(executable_path='C:/Users/emman/Desktop/stuff/edgedriver_win64/msedgedriver.exe')
driver.get("https://2anki.net/upload")
driver.maximize_window()

path ="C:\\Users\\emman\\Documents\\To Anki"
directory= os.listdir(path) 


# print(f"The current working directory is {os.getcwd()}")
# os.chdir("C:\\Users\\emman\\Projects\\notion_anki_auto")
# print(f"The current working directory is {os.getcwd()}")

# path ="C:\\Users\\emman\\Projects\\notion_anki_auto" 

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
    
def convert_notion_to_anki():
    # using web scraping 

    # Go to the web page and edit the options to enable avocado and some

    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/a').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[2]/section/div/div[2]/div/label[6]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/button[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/form/div/div/div/div/label/span').click()

    #loop throug the items to be uploaded, excluding the "Exported folder", upload them to the site
    for item in directory:
        print(item)
        if item == "Exported":
            print("This is the 'Exported' folder, NO TRESPASSING ")
            pass
        else:
            print("This is a not the 'Exported' folder, Carry on")
            #upload them to the site 



# print(check_for_new_decks())

if check_for_new_decks() == "Empty":
    print("No new decks")
else:
    convert_notion_to_anki()
