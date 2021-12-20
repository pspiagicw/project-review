from prompt_toolkit import prompt
from random import random
import cv2
import hashlib
import os
from shortifydata import *
from moviepy.editor import *
from unsilence import Unsilence
from tqdm import tqdm

def getInputs():
    filename = prompt('Enter the filename[mp4]: ')
    print('Using File: {}'.format(filename))
    frames_per_second = prompt('Enter the fps to consider[default(24)]: ')
    if frames_per_second == '':
        frames_per_second = 24
    print('Using Frames Per Second: {}'.format(frames_per_second))
    interval = prompt('Enter interval between checks[default(15)]: ')
    if interval == '':
        interval = 15
    print('Using Interval: {}'.format(interval))
    if not os.path.isfile(filename):
        print("File {} does not exist!".format(filename))
        exit(1)
    return filename , frames_per_second , interval

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
                clips.append((getStatus(frame) , seconds))
            seconds += 1
        counter += 1
    video.release()
    return clips , seconds
def clipVideo(sourcepath , starts , ends , filepath):
    video = VideoFileClip(sourcepath)
    for i , (start , end) in enumerate(zip(starts , ends)):
        clip = video.subclip(start , end)
        savepath = os.path.join(filepath ,str(i) + '.mp4')
        clip.write_videofile(savepath)

def getPreFilePath(filename):
    new_file_name = ''.join(hashlib.sha512(filename.encode('utf-8')).hexdigest()[:5])
    dir = os.path.join('tmp' , 'preprocess')
    filepath = os.path.join(dir , new_file_name)
    os.mkdir(filepath)
    return filepath

def getPostFilePath(filename):
    new_file_name = ''.join(hashlib.sha512(filename.encode('utf-8')).hexdigest()[:5])
    dir = os.path.join('tmp' , 'postprocess')
    filepath = os.path.join(dir , new_file_name)
    os.mkdir(filepath)
    return filepath

def silenceClips(filepath , outputPath):
    files = sorted(os.listdir(filepath))
    for i , file in tqdm(enumerate(files)):
         filename = os.path.join(filepath , file)
         u = Unsilence(filename)
         u.detect_silence()
         u.estimate_time(audible_speed=2, silent_speed=1)  # Estimate time savings
         file_save_location = os.path.join(outputPath , file)
         u.render_media(file_save_location , silent_volume = 4 , audible_volume = 7)
def combineClips(inputPath):
    files = sorted(os.listdir(inputPath))
    final_clip = concatenate_videoclips([
        VideoFileClip(os.path.join(inputPath , file)) for file in files
        ])
    final_clip.write_videofile("output.mp4")



def makeDirs(dir1 , dir2):
    os.mkdir(dir1)
    os.mkdir(dir2)
