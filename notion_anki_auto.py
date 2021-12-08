import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from apscheduler.schedulers.background import BackgroundScheduler




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

# print(check_for_new_decks())

if check_for_new_decks() == "Empty":
    print("No new decks")
else:

    driver = webdriver.Edge(executable_path='C:/Users/emman/Desktop/stuff/edgedriver_win64/msedgedriver.exe')
    driver.get("https://2anki.net/upload")
    driver.maximize_window()

    convert_notion_to_anki()
    print("Converted")


# def check_and_convert():
#     if check_for_new_decks() == "Empty":
#         print("No new decks")
#     else:
#         convert_notion_to_anki()
#         print("Converted")

# def scheduler_test():
#     print("Scheduler Working")


# def start():
#     scheduler = BackgroundScheduler()
#     """TESTING"""
#     scheduler.add_job(scheduler_test, 'cron', hour='12,14,17',
#                       minute='0,5,10,15,20,25,34,35,38', )

#     """chron not assigned"""

#     """WORKING"""
#     # Runs in 1:00am everyday
#     scheduler.add_job(check_and_convert, 'interval', minutes=30)
#     print("Scheduler started...", file=sys.stdout)