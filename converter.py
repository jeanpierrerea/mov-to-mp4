import os

# Script to convert MOV files into MP4 files using ffmpeg because i am lazy 

# Collecting filename from user 
def fileName():
    fileName = input ('Enter filename: ')
    return fileName

# ffmpeg -i vidName.mov -vcodec h264 -acodec mp2 outName.mp4
# command that I used to convert videos manually

def convert_mov_mp4(name):
    command = 'ffmpeg -i "./%s.mov" -vcodec h264 -acodec mp2 "./%s.mp4"' % (name, name)
    return command


command = convert_mov_mp4(fileName())

# opens cmd and runs the command

os.system('cmd /k ' + command)