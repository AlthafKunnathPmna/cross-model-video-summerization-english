import easyocr
import os

reader = easyocr.Reader(['en'])

def extract_slide_logic(frame_dir, max_frames=5):
    slide_points = []

    frames = sorted(os.listdir(frame_dir))[:max_frames]
    for frame in frames:
        results = reader.readtext(
            os.path.join(frame_dir, frame)
        )

        for bbox, text, conf in results:
            if conf > 0.6 and len(text) > 4:
                slide_points.append(text)

    unique = list(dict.fromkeys(slide_points))
    return " • ".join(unique)

