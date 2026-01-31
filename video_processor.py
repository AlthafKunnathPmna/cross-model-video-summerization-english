# import os
# import ffmpeg

# # def extract_frames(video_path, fps=1):
# #     os.makedirs("temp/frames", exist_ok=True)

# #     (
# #         ffmpeg
# #         .input(video_path)
# #         .filter("fps", fps=fps)
# #         .output("temp/frames/frame_%04d.jpg")
# #         .overwrite_output()
# #         .run(quiet=True)
# #     )

# def extract_frames(video_path, fps=1):
#     os.makedirs("temp/frames", exist_ok=True)

#     try:
#         (
#             ffmpeg
#             .input(video_path)
#             .filter("fps", fps=fps)
#             .output("temp/frames/frame_%04d.jpg")
#             .overwrite_output()
#             .run(capture_stdout=True, capture_stderr=True)
#         )
#     except ffmpeg.Error as e:
#         print("FFmpeg stdout:", e.stdout.decode())
#         print("FFmpeg stderr:", e.stderr.decode())
#         raise


# def extract_audio(video_path):
#     (
#         ffmpeg
#         .input(video_path)
#         .output("temp/audio.wav", ac=1, ar="16k")
#         .overwrite_output()
#         .run(quiet=True)
#     )



# import os
# import ffmpeg
# import imageio_ffmpeg

# # Get bundled FFmpeg binary (works on Streamlit Cloud)
# FFMPEG_BINARY = imageio_ffmpeg.get_ffmpeg_exe()


# def extract_frames(video_path, fps=1):
#     os.makedirs("temp/frames", exist_ok=True)

#     try:
#         (
#             ffmpeg
#             .input(video_path)
#             .filter("fps", fps=fps)
#             .output("temp/frames/frame_%04d.jpg")
#             .overwrite_output()
#             .run(
#                 cmd=FFMPEG_BINARY,
#                 capture_stdout=True,
#                 capture_stderr=True
#             )
#         )
#     except ffmpeg.Error as e:
#         print("❌ FFmpeg frame extraction failed")
#         print("STDOUT:", e.stdout.decode() if e.stdout else "")
#         print("STDERR:", e.stderr.decode() if e.stderr else "")
#         raise


# def extract_audio(video_path):
#     os.makedirs("temp", exist_ok=True)

#     try:
#         (
#             ffmpeg
#             .input(video_path)
#             .output("temp/audio.wav", ac=1, ar="16000")
#             .overwrite_output()
#             .run(
#                 cmd=FFMPEG_BINARY,
#                 capture_stdout=True,
#                 capture_stderr=True
#             )
#         )
#     except ffmpeg.Error as e:
#         print("❌ FFmpeg audio extraction failed")
#         print("STDOUT:", e.stdout.decode() if e.stdout else "")
#         print("STDERR:", e.stderr.decode() if e.stderr else "")
#         raise


import os
import ffmpeg
import imageio_ffmpeg

# Use bundled FFmpeg binary (NO system FFmpeg needed)
FFMPEG_BINARY = imageio_ffmpeg.get_ffmpeg_exe()


def extract_frames(video_path, fps=1):
    frames_dir = os.path.abspath("temp/frames")
    os.makedirs(frames_dir, exist_ok=True)

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    if os.path.getsize(video_path) == 0:
        raise ValueError("Uploaded video file is empty")

    try:
        ffmpeg.input(video_path).filter(
            "fps", fps=fps
        ).output(
            os.path.join(frames_dir, "frame_%04d.jpg")
        ).overwrite_output().run(
            cmd=FFMPEG_BINARY,
            capture_stdout=True,
            capture_stderr=True
        )

    except ffmpeg.Error as e:
        print("========== FFMPEG FRAME ERROR ==========")
        print("STDOUT:", e.stdout.decode(errors="ignore") if e.stdout else "")
        print("STDERR:", e.stderr.decode(errors="ignore") if e.stderr else "")
        print("=======================================")
        raise


def extract_audio(video_path):
    audio_dir = os.path.abspath("temp")
    os.makedirs(audio_dir, exist_ok=True)

    try:
        ffmpeg.input(video_path).output(
            os.path.join(audio_dir, "audio.wav"),
            ac=1,
            ar="16000"
        ).overwrite_output().run(
            cmd=FFMPEG_BINARY,
            capture_stdout=True,
            capture_stderr=True
        )

    except ffmpeg.Error as e:
        print("========== FFMPEG AUDIO ERROR ==========")
        print("STDOUT:", e.stdout.decode(errors="ignore") if e.stdout else "")
        print("STDERR:", e.stderr.decode(errors="ignore") if e.stderr else "")
        print("=======================================")
        raise
