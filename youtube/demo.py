from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def split_video(inp, out_dr, duration=60):
    # Load video
    video = VideoFileClip(inp)

    video_len = int(video.duration)

    clip = (video_len // duration) + 1
    

    # split video
    for i in range(clip):
        start_time = i * duration
        end_time = min((i+1)*duration, video_len)
        

inp = "C:/Users/Owner/Videos/Captures/Mood mappers - Brave 2023-07-19 23-08-04.mp4"
dir = "D:/D/Certification/Projects/Money handle/youtube/clips"
split_video(inp, dir)