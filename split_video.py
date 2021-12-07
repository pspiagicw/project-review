from prompt_toolkit import prompt
from random import random
import cv2
import hashlib
import os

def getInputs():
    filename = prompt('Enter the filename[mp4]: ')
    print(filename)
    frames_per_second = prompt('Enter the fps to consider[default(30)]: ')
    print(frames_per_second)
    interval = prompt('Enter interval between checks: ')
    return filename , frames_per_second , interval

def getStatus(picture):
    return random() > 0.5

def getTimings(filename  , fps , interval):
    video = cv2.VideoCapture(filename)
    clips = list()
    counter = 0
    seconds = 0
    while True:
        ret , frame = video.read()
        if ret == False:
            break
        if counter % fps == 0:
            if seconds % interval == 0:
                clips[-1].append((getStatus(frame) , seconds))
            seconds += 1
        counter += 1
    video.release()
    return clips

def clipVideo(sourcepath , starts , ends , filepath):
    video = VideoFileClip(sourcepath)
    for i , start , end in enumerate(zip(starts , ends)):
        clip = video.subclip(start , end)
        savepath = os.path.join(filepath ,str(i) + '.mp4')
        clip.write_videofile(savepath)

def getPreFilePath(filename):
    new_file_name = ''.join(hashlib.sha512(filename.encode('utf-8')).hexdigest()[:5])
    dir = os.path.join('tmp' , 'preprocess')
    filepath = os.path.join(dir , new_file_name)
    return filepath

def getPostFilePath(filename):
    new_file_name = ''.join(hashlib.sha512(filename.encode('utf-8')).hexdigest()[:5])
    dir = os.path.join('tmp' , 'postprocess')
    filepath = os.path.join(dir , new_file_name)
    return filepath

def silenceClips(filepath , outputPath):
    files = sorted(os.listdir(filepath))
    for i , file in enumerate(files):
         u = Unsilence(file)
         file_save_location = os.path.join(outputPath , file + str(i) + '.mp4')
         u.render_media(save_file_location , silent_volume = 4 , audible_volume = 7)
def combineClips(inputPath):
    files = sorted(os.listdir(inputPath))
    final_clip = concatenate_videoclips([
        VideoFileClip(os.path.join(inputPath , file)) for file in files
        ])
    final_clip.write_videofile("output.mp4")



