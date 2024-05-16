import pyautogui as pg
import time
import webbrowser
import os
import random
import datetime
import logging

from emailKYLE import sendlogTOkyle

logging.basicConfig(level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='auto.log', filemode='w')


#defaultAnswer
def questionString(question, defaultAnswer):
    answer = input(f"{question} [{defaultAnswer}]")
    if answer == "":
        answer = defaultAnswer
    return answer 

#open instagram
def openInstagram():
    webbrowser.open('https://www.instagram.com/')
    time.sleep(10)

#open post
def OpenPost():
    pg.moveTo(31, 584, duration = 0)
    pg.click()
    time.sleep(2)
    pg.moveTo(138, 623, duration = 0)
    pg.click()

#select meme
def select_random_meme(folder_path):
    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        logging.error("No meme images found in the folder.")
        return None
    random_meme = random.choice(image_files)
    return random_meme

#select meme
def meme():
    meme_folder_path = "memes"

    random_meme_name = select_random_meme(meme_folder_path)
    if random_meme_name:
        logging.info(f"Selected meme: {random_meme_name}")
        ChoseMeme(random_meme_name)

#chose meme
def ChoseMeme(random_meme_name):
    time.sleep(1)
    pg.moveTo(520, 510, duration = 1)
    pg.click()
    pg.moveTo(485, 47, duration = 1)
    time.sleep(1)
    pg.click()
    pg.typewrite("C:\\Users\\win10_64\\Desktop\\memes")
    pg.press("enter")
    pg.moveTo(469, 667, duration = 1)
    pg.click()
    time.sleep(1)
    pg.typewrite(random_meme_name)
    time.sleep(1)
    pg.press("enter")

#load meme
def lodeMeme():
    pg.moveTo(336, 609, duration = 1)
    pg.click()
    pg.moveTo(372, 396, duration = 1)
    pg.click()
    pg.moveTo(675, 227, duration = 1)
    pg.click()
    time.sleep(1)
    pg.moveTo(847, 227, duration = 1)
    pg.click()

#write caption
def WriteCaption():
    captions = [
        "Bug squashed, another arises", 
        "Risking it all with an update", 
        "Break? Just switch code types", 
        "Not a bug, a feature!", 
        "When your code finally works on the first try!", 
        "That moment you realize it's not a bug, just a feature", 
        "Me, when I see a semicolon missing :o", 
        "Sleep is for the weak; debugging is for the strong",
        "When you finally fix that bug that's been bugging you for days",
        "When you finally understand recursion. Mind. Blown.",
        "My code isn't messy; it's just creatively organized!",
        "Sleep? I'll do that after this next commit.",
        "Coffee: Fueling developers since the beginning of time.",
        "I don't always test my code, but when I do, I do it in production.",
        "When you're coding and you realize you've been talking to yourself for the past 20 minutes.",
        "what do you mean, 'it works on my machine'?",
        "how did this ever work?",
        "I'm not anti-social; I'm just not user friendly."
    ]
    
    hashtags = [
        "#CodeHumor", "#GeekHumor", "#TechJokes", "#DevLife", 
        "#ProgrammerLife", "#ProgrammingHumor", "#ProgrammingJokes", 
        "#ProgrammerHumor", "#SoftwareDeveloper", "#SoftwareEngineer", 
        "#SoftwareDevelopment", "#SoftwareEngineerLife", "#SoftwareEngineerProblems", 
        "#SoftwareEngineerHumor", "#SoftwareEng" ,"#SoftwareEngineering", 
        "#programming", "#joke", "#funny", "#coding", "#programmer", "#developer", 
        "#codinglife", "#webdeveloper", "#webdevelopment", 
        "#webdev", "#webdesign", "#webdesigner", "#webdesigning", 
        "#webdesignlife", "#webdesignerlife", "#webdesigners", 
        "#webdesignerslife", "#webdesignersofinstagram", "#webdesignersofinsta", 
        "#webdesignersoftheworld", "#webdesignersoftheworld", "#webdesignersoftheworldunite"
    ]

    random_caption = random.choice(captions)
    random_hashtag = random.choice(hashtags)
    random_hashtag2 = random.choice(hashtags)
    random_hashtag3 = random.choice(hashtags)

    logging.info("Choosing caption and hashtags")
    # Write the caption
    pg.moveTo(576, 322, duration=0)
    pg.click()
    pg.typewrite(f"{random_caption}")
    logging.info({random_caption})
    time.sleep(1)

    # Write the hashtag
    pg.press("enter")
    pg.typewrite(f"{random_hashtag}")
    logging.info({random_hashtag})
    pg.moveTo(599, 548, duration=0)
    time.sleep(1.5)
    pg.click()
    
    # Write the hashtag2
    time.sleep(1)
    pg.typewrite(f"{random_hashtag2}")
    logging.info({random_hashtag2})
    pg.moveTo(599, 548, duration=0)
    time.sleep(1.5)
    pg.click()

    # Write the hashtag3
    time.sleep(1)
    pg.typewrite(f"{random_hashtag3}")
    logging.info({random_hashtag3})
    pg.moveTo(599, 548, duration=0)
    time.sleep(1.5)
    pg.click()

    # Write the disclaimer
    time.sleep(1)
    pg.moveTo(818, 454, duration=0)
    time.sleep(0.5)
    pg.press("enter")
    pg.typewrite("This post was made and uploaded by a python bot :D")

#post meme
def postMeme():
    pg.moveTo(840, 231, duration=0)
    pg.click()

    #close window
    time.sleep(1)
    pg.moveTo(975, 145, duration=0)
    time.sleep(2)
    pg.click()
    pg.moveTo(1007, 19, duration=0)
    time.sleep(1)
    pg.click()

#main code
def main_sequence():
    openInstagram()
    logging.info("Instagram opened")
    time.sleep(1)
    OpenPost()
    logging.info("Post menu opened")
    time.sleep(1)
    meme()
    logging.info("Meme selected")
    time.sleep(1)
    lodeMeme()
    logging.info("Meme loaded") 
    time.sleep(1)
    WriteCaption()
    logging.info("Caption written")
    time.sleep(1)
    postMeme()
    logging.info("Meme posted")
    logging.critical("Script ended")


logging.info("Script running at " + str(datetime.datetime.now()))
logging.info(f"The screen size is: {pg.size()}")
main_sequence()
logging.info("Script ended at:  " + str(datetime.datetime.now()))
#os.startfile("auto.log", "print")
#os.startfile("auto.log")
sendlogTOkyle()
time.sleep(5)