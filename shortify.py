import shutil
import os
from libshortify import *


def cleanDir():
    if os.path.isdir('tmp'):
        shutil.rmtree('tmp')
    os.mkdir('tmp')
    os.mkdir('tmp/preprocess')
    os.mkdir('tmp/postprocess')

if __name__ == '__main__':

    cleanDir()

    # filename , fps , interval = getInputs()
    filename , fps , interval = 'meeting.mp4' , 30 , 15

    preprocessing_dir = getPreFilePath(filename)

    postprocessing_dir = getPostFilePath(filename)

    print(type(filename))
    print(type(fps))
    print(type(interval))

    timings = getTimings(filename , int(fps) , int(interval))

    starts , ends = analyzeTimings(timings , int(fps) , int(interval))

    clipVideo(filename , starts , ends , preprocessing_dir )

    silenceClips(preprocessing_dir , postprocessing_dir)

    combineClips(postprocessing_dir)
    

    
    


