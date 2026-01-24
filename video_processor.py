import os
import ffmpeg

def extract_frames(video_path, fps=1):
    os.makedirs("temp/frames", exist_ok=True)

    (
        ffmpeg
        .input(video_path)
        .filter("fps", fps=fps)
        .output("temp/frames/frame_%04d.jpg")
        .overwrite_output()
        .run(quiet=True)
    )

def extract_audio(video_path):
    (
        ffmpeg
        .input(video_path)
        .output("temp/audio.wav", ac=1, ar="16k")
        .overwrite_output()
        .run(quiet=True)
    )
