from random import random
from keras.models import load_model
import cv2
def getStatus(picture , pixel_differenciation = False):
    model = load_model('model')
    resized_image = cv2.resize(picture , (800 , 600))
    status = model.predict([resized_image])
    return status[0] > 0.5
def analyzeTimings(timings , fps , interval):
    print(timings)
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
    return [ i[0] for i in analyzedtimings ] , [ i[1] for i in analyzedtimings ]

