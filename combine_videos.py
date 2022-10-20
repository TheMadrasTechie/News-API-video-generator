from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def video_make():
	aa = []
	path = "videos"
	dir_list = os.listdir(path)
	for i in dir_list:	
		aa.append(VideoFileClip("videos/"+i))	
	final_clip = concatenate_videoclips(aa)
	final_clip.write_videofile("final.mp4")
	for i in dir_list:	
		os.remove("videos/"+i)