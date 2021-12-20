from random import random
from tabulate import tabulate
from colorama import Fore , Back , Style
from tensorflow.keras.models import load_model
import cv2
import numpy as np
def getStatus(picture , pixel_differenciation = False):
    model = load_model('model')
    resized_image = cv2.resize(picture , (600 , 800))
    resized_image = cv2.cvtColor(resized_image , cv2.COLOR_BGR2RGB)
    status = model.predict(np.asarray([resized_image]))
    return status[0] > 0.5
def analyzeTimings(timings , fps , interval):
    analyzedtimings = list()
    previous = False
    start = 0
    end = None
    for time in timings:
        if time[0] != previous:
            if time[0] == True:
                start = time[1]
            if time[0] == False:
                end = time[1]
                analyzedtimings.append((start , end ))
        previous = time[0]
    prettyPrint(analyzedtimings)
    return [ i[0] for i in analyzedtimings ] , [ i[1] for i in analyzedtimings ]
def prettyPrint(atimings):
    print(Fore.GREEN + "Your video file will be divided into {} parts!".format(len(atimings)) + Style.RESET_ALL)
    print(Fore.RED + tabulate(atimings , headers=['Start(seconds)' , 'End(seconds)'] , tablefmt="fancy_grid") + Style.RESET_ALL)
   
def prettyPrintSeconds(second , timings , fps , frame_counter):
    print(Fore.GREEN + "Your video file contains {} seconds of footage at {}fps!".format(second , fps) + Style.RESET_ALL)
    print(Fore.GREEN + "We analyzed {} frames to determine this!".format(frame_counter) + Style.RESET_ALL)
    used = sum(j-i for (i , j) in timings)
    saved = second - used
    print(Fore.GREEN + "You have saved {} seconds by removing lobby scenes! Starting processing in 5 seconds".format(saved) + Style.RESET_ALL)
    time.sleep(5)

def prettyPrintBanner():
    print(Fore.BLUE + """
     _______. __    __    ______   .______      .___________. __   _______ ____    ____ 
    /       ||  |  |  |  /  __  \  |   _  \     |           ||  | |   ____|\   \  /   / 
   |   (----`|  |__|  | |  |  |  | |  |_)  |    `---|  |----`|  | |  |__    \   \/   /  
    \   \    |   __   | |  |  |  | |      /         |  |     |  | |   __|    \_    _/   
.----)   |   |  |  |  | |  `--'  | |  |\  \----.    |  |     |  | |  |         |  |     
|_______/    |__|  |__|  \______/  | _| `._____|    |__|     |__| |__|         |__|     
                                                                                        
    """ + Style.RESET_ALL)
    print("Welcome to Shortify! Enter details of the video below!")
    

