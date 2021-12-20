import shutil
import os
from libshortify import *
from shortifydata import *
import time


def cleanDir():
    if os.path.isdir('tmp'):
        shutil.rmtree('tmp')
    os.mkdir('tmp')
    os.mkdir('tmp/preprocess')
    os.mkdir('tmp/postprocess')

if __name__ == '__main__':

    cleanDir()

    prettyPrintBanner()
    filename , fps , interval = getInputs()
    # filename , fps , interval = 'meeting.mp4' , 30 , 15

    preprocessing_dir = getPreFilePath(filename)

    postprocessing_dir = getPostFilePath(filename)


    timings , seconds = getTimings(filename , int(fps) , int(interval))


    starts , ends = analyzeTimings(timings , int(fps) , int(interval))

    prettyPrintSeconds(seconds  , [i for i in zip(starts , ends)] , fps)

    time.sleep(5)

    clipVideo(filename , starts , ends , preprocessing_dir )

    silenceClips(preprocessing_dir , postprocessing_dir)

    combineClips(postprocessing_dir)
    

    
    


