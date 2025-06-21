from moviepy.editor import VideoFileClip
import math
import os

def split_video(inp_path, out_dir, chunk_len=780):
    # Ensure output directory exists
    os.makedirs(out_dir, exist_ok=True)

    # Open the video safely
    with VideoFileClip(inp_path) as video:
        total_sec = int(video.duration)
        n_chunks = math.ceil(total_sec / chunk_len)

        for i in range(n_chunks):
            start = i * chunk_len
            end   = min((i + 1) * chunk_len, total_sec)

            out_file = os.path.join(out_dir, f'clip_{i + 1}.mp4')
            (video.subclip(start, end)
                  .write_videofile(out_file,
                                   codec="libx264",
                                   audio_codec="aac",
                                   temp_audiofile="temp-audio.m4a",
                                   remove_temp=True))
            print(f"Saved {out_file}")

# Example usage
inp_path = r"D:\D\Projects\Money handle\youtube\clips\clip_1.mp4"
out_dir  = r"D:\D\Projects\Money handle\youtube\video_clip"

split_video(inp_path, out_dir)
