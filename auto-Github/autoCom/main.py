import pyautogui as pg
import time
import webbrowser
import datetime
import logging

#set wait time
wait = 1

#set logging
logging.basicConfig(level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='git.log', filemode='w')

#open Github
def openGit():
    webbrowser.open('https://github.com/KyleSeaford/KyleSeaford/edit/main/Everyday')
    time.sleep(wait)
    logging.info("Github open")

#update
def update(): 
    pg.moveTo(2606, 578, duration = 1)
    pg.click()
    time.sleep(wait)
    pg.typewrite(f"Update: {datetime.datetime.now()}")
    logging.info("Updated github")

#save
def save():
    pg.moveTo(3686, 208, duration=1)
    pg.click()
    pg.moveTo(2838, 416, duration=1)
    pg.click()
    time.sleep(0.2)
    pg.click()
    time.sleep(0.2)
    pg.click()
    pg.typewrite(f"Update Everyday - {datetime.datetime.now()}")
    time.sleep(wait)
    pg.moveTo(3011, 764, duration=1)
    pg.click()
 
#back home
def home():
    pg.moveTo(2080, 102, duration=1)
    pg.click()

def main():
    logging.info("SCRIPT STARTED")
    openGit()
    update()
    save()
    home()
    logging.info("SCRIPT ENDED")


main()