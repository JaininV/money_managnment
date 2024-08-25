from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def split_video(inp, out_dr, duration=60):
    # Load video
    video = VideoFileClip(inp)

    video_len = int(video.duration)
    print(video_len)

inp = "D:/D/Certification/Projects/Money handle/youtube/yt1s.com - 4K Planet Earth Spinning in Space  Free HD Videos  No Copyright_1080p.mp4"
dir = "D:/D/Certification/Projects/Money handle/youtube/clips"
split_video(inp, dir, )