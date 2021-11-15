## Single Videos ##
#   This script is for single video downloads only.
#   It utilizes the DASH .itag() pytube library


## Why not just use .first() instead of itag()?
#   I have run multiple video download tests and using .first() is unreliable for good quality
#   Hardcoding and iterating over the video qualities (from best to worst) is the better option
# Ex: using .first()
# pytube.YouTube(link).streams.filter(file_extension = "mp4").first().download(skip_existing=True, output_path="C:\\PATH\\TO\\OUTPUT")


import pytube
import os


# Here is a list of the .itag() numbers
# https://github.com/pytube/pytube/blob/master/pytube/itags.py

# DASH .itag() numbers, you can add to this list if the video is low quality
viditag = [571, 402, 399, 398, 397, 299, 298, 266, 264, 138, 137, 136, 135, 22]
auditag = [258, 256, 141, 140, 139]
# exception to this list: darude sandstorm video, downloaded the audio, NO video


# Put your link here
link = "https://www.youtube.com/watch?v=Mu8AcdQlApw"


# Download the Video
def videoDL():
    count = 0
    for vidi in viditag:
        try:
            pytube.YouTube(link).streams.filter(file_extension = "mp4").get_by_itag(vidi).download(skip_existing=True, output_path="C:\\PATH\\TO\\video")
            count += 1
        except:
            print(str(vidi) + " itag not found")
            if count > 1:
                break

# Download the Audio
def audioDL():
    counta = 0
    for audi in auditag:
        try:
            pytube.YouTube(link).streams.filter(file_extension = "mp4").get_by_itag(audi).download(skip_existing=True, output_path="C:\\PATH\\TO\\nonwavtmp")
            counta += 1
        except:
            print(str(audi) + " itag not found")
            if counta > 1:
                break


def completer():

    videoDL()
    audioDL()


    vidpath = "C:\\PATH\\TO\\video\\"
    vidfiles = os.listdir(vidpath)

    def vidpass():
        for xvidi in range(0,len(vidfiles)):
            totle = os.listdir(vidpath)[xvidi]
            vidtitlespaces = totle.find(" ")
            if vidtitlespaces >= 0:
                totle2 = totle.replace(",", "")
                totle2 = totle.replace("?", "")
                totle2 = totle.replace("/", "")
                totle2 = totle.replace("-", "")
                totle2 = totle.replace("!", "")
                totle2 = totle.replace("'", "")
                totle2 = totle.replace('"', '')
                totle2 = totle.replace(" ", "")
                os.rename("C:\\PATH\\TO\\video\\" + totle,"C:\\PATH\\TO\\video\\" + totle2)


    audipath = "C:\\PATH\\TO\\nonwavtmp\\"
    audifiles = os.listdir(audipath)

    def audiopass():
        for xaudi in range(0,len(audifiles)):
            audititle = os.listdir(audipath)[xaudi]
            audititlespaces = audititle.find(" ")
            if audititlespaces >= 0:
                totle4 = audititle.replace(",", "")
                totle4 = audititle.replace("?", "")
                totle4 = audititle.replace("/", "")
                totle4 = audititle.replace("-", "")
                totle4 = audititle.replace("!", "")
                totle4 = audititle.replace("'", "")
                totle4 = audititle.replace('"', '')
                totle4 = audititle.replace(" ", "")
                os.rename("C:\\PATH\\TO\\nonwavtmp\\" + audititle,"C:\\PATH\\TO\\nonwavtmp\\" + totle4)

    # Gets all filenames in audipath DIR
    # Chops off .mp4 extension for FFmpeg command line
    # Converts file.mp4 -> file.wav
    def audioconversion():
        for xaudi in range(0,len(audifiles)):
            # Iterates over the filenames in the DIR
            audititle2 = os.listdir(audipath)[xaudi]
            wer = audititle2[:audititle2.index(".")]
            os.system("C:\\PATH\\TO\\FFmpeg\\EXE\\ffmpeg-N-104544-gbfbd5954e5-win64-gpl\\bin\\ffmpeg -i C:\\PATH\\TO\\nonWAVtmp\\" + audititle2 + " -b:a 192K -vn C:\\PATH\\TO\\audio\\" + wer +".wav")
            print("AUDIO CONVERTED")

            
    vidpass()
    audiopass()
    audioconversion()


# Combines both the audio and video files
def comp():
    vidpath2 = "C:\\PATH\\TO\\video\\"
    audipath2 = "C:\\PATH\\TO\\audio\\"
    vidfiles2 = os.listdir(vidpath2)
    audifiles2 = os.listdir(audipath2)

    for x in range(0,len(vidfiles2)):
        vidfiles3 = os.listdir(vidpath2)[x]
        audifiles3 = os.listdir(audipath2)[x]
        os.system("C:\\PATH\\TO\\FFmpeg\\EXE\\ffmpeg-N-104544-gbfbd5954e5-win64-gpl\\bin\\ffmpeg -i C:\\PATH\\TO\\video\\" + vidfiles3 +" -i C:\\PATH\\TO\\audio\\" + audifiles3 +" -c:v copy -c:a aac C:\\PATH\\TO\\combinationAV\\" + vidfiles3 +".mp4")
        print("VIDEO COMPILED")


def garbagecollection():
    garbaudiotmp = "C:\\PATH\\TO\\nonwavtmp\\"
    garbvideo = "C:\\PATH\\TO\\video\\"
    garbaudio = "C:\\PATH\\TO\\audio\\"
    audiotmpgarb = os.listdir(garbaudiotmp)[0]
    vidgarb = os.listdir(garbvideo)[0]
    audiogarb = os.listdir(garbaudio)[0]

    if os.path.exists("C:\\PATH\\TO\\nonwavtmp\\" + str(audiotmpgarb)):
        os.remove("C:\\PATH\\TO\\nonwavtmp\\" + audiotmpgarb)
    else:
        print("The audio tmp file does not exist")

    if os.path.exists("C:\\PATH\\TO\\video\\" + str(vidgarb)):
        os.remove("C:\\PATH\\TO\\video\\" + vidgarb)
    else:
        print("The video file does not exist") 

    if os.path.exists("C:\\PATH\\TO\\audio\\" + str(audiogarb)):
        os.remove("C:\\PATH\\TO\\audio\\" + audiogarb)
    else:
        print("The audio file does not exist") 
        

completer()
comp()
# garbagecollection()
