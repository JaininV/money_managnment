from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def split_video(inp, out_dr, duration=600):
    # Load video
    video = VideoFileClip(inp)
    print(video)
    video_len = int(video.duration)

    clip = (video_len // duration) + 1
    

    # split video
    for i in range(clip):
        start_time = i * duration
        end_time = min((i+1)*duration, video_len)

        sub_clip = video.subclip(start_time, end_time)
        out_file = os.path.join(out_dr, f'clip_{i+1}.mp4')

        sub_clip.write_videofile(out_file, codec="libx264", audio_codec="aac")
        print(f"Saved {out_file}")

    print("Video splitting")        

inp = "D:/F/Family/highlight.mp4"
dir = "D:/D/Certification/Projects/Money handle/youtube/clips"
split_video(inp, dir)