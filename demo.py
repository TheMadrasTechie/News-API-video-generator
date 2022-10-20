from newsapi import NewsApiClient
from gtts import gTTS
import urllib.request
import cv2
import numpy as np
import time
import video
import os
import combine_videos

def text_speech(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("audio\\audio_file.mp3")

# Init
newsapi = NewsApiClient(api_key='4dbc17e007ab436fb66416009dfb59a8')

author = []
title = []
description = []
url = []
urlToImage = []
publishedAt = []
content = []


# business entertainment health science sports technology
top_headlines = newsapi.get_top_headlines(category='technology',country='us',page_size=10)



for i in range(len(top_headlines['articles'])):
    print(i)
    print(top_headlines['articles'][i]['title'])
    print(top_headlines['articles'][i]['description'])
    author.append(top_headlines['articles'][i]['author'])
    title.append(top_headlines['articles'][i]['title'])
    description.append(top_headlines['articles'][i]['description'])
    url.append(top_headlines['articles'][i]['url'])
    urlToImage.append(top_headlines['articles'][i]['urlToImage'])
    publishedAt.append(top_headlines['articles'][i]['publishedAt'])
    content.append(top_headlines['articles'][i]['content'])
    try:
            print(top_headlines['articles'][i]['urlToImage'])
            data = urllib.request.urlretrieve(top_headlines['articles'][i]['urlToImage'], "images/"+"tmp"+".jpg")
            time.sleep(2)
            img = cv2.imread("images/"+"tmp"+".jpg")
            s = max(img.shape[0:2])
            f = np.zeros((s,s,3),np.uint8)
            f[f==0]=255
            ax,ay = (s - img.shape[1])//2,(s - img.shape[0])//2
            f[ay:img.shape[0]+ay,ax:ax+img.shape[1]] = img
            f = cv2.resize(f,(1080,1080))
            cv2.imwrite("images/"+"tmp"+".png",f) 
            text_speech(top_headlines['articles'][i]['title']+". . . ..... ."+top_headlines['articles'][i]['description'])
            time.sleep(2)
            video.MP3ToMP4('images', 'audio/audio_file.mp3', 'videos/video'+str(i)+'.mp4')            
            
            
    except:
            print("issue")


combine_videos.video_make()

#title = " ... ".join(title)
#text_speech(title)