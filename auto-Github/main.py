import pyautogui as pg
import time
import webbrowser
import datetime
import logging

from mailSeaford import emailTOKyle

#set wait time
wait = 2

#set logging
logging.basicConfig(level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='git.log', filemode='w')

#open Github
def openGit():
    time.sleep(wait)
    webbrowser.open('https://github.com/KyleSeaford/KyleSeaford/edit/main/Everyday')
    time.sleep(wait)
    logging.info("Github opened")

#update
def update(): 
    pg.moveTo(2606, 578, duration = 1)                                                          #clicks blank space
    pg.click()
    logging.info("clicked blank space")
    time.sleep(wait)
    pg.typewrite(f"Update: {datetime.datetime.now()}")
    logging.info("Updated github repository")

#save
def save():
    pg.moveTo(3686, 208, duration=1)                                                            #clicks 'commit changes'         
    pg.click()
    logging.info("clicked 'commit changes'")
    pg.moveTo(2838, 416, duration=1)                                                            #clicks in the message box
    pg.click()
    logging.info("clicked in the message box")
    time.sleep(0.2)
    pg.click()                                                                                  #triple clicks to select all
    time.sleep(0.2)
    pg.click()
    pg.typewrite(f"Update Everyday - {datetime.datetime.now()}")                                #types the commit message
    logging.info("typed the commit message")
    time.sleep(wait)
    pg.moveTo(3011, 764, duration=1)                                                            #clicks 'commit changes'
    pg.click()
    logging.info("clicked 'commit changes'")
 
#back home
def home():
    pg.moveTo(2080, 102, duration=1)                                                            #clicks 'KyleSeaford' in top left
    pg.click()
    logging.info("clicked 'KyleSeaford' in top left")
    
#main script
def main():
    logging.warning("SCRIPT STARTED")
    openGit()
    update()
    save()
    home()
    logging.warning("SCRIPT ENDED")


#run script

logging.info("Script running at " + str(datetime.datetime.now()))
logging.info(f"The screen size is: {pg.size()}")
main()
emailTOKyle()