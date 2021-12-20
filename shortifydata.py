from random import random
def getStatus(picture , pixel_differenciation = False):
    return random() > 0.5
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

