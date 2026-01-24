import whisper
import re

model = whisper.load_model("base")

def clean_text(text):
    fillers = ["uh", "um", "you know", "okay", "so"]
    for f in fillers:
        text = text.replace(f, "")
    return re.sub(r"\s+", " ", text).strip()

def extract_important_audio(audio_path):
    result = model.transcribe(audio_path)
    important = []

    for seg in result["segments"]:
        text = seg["text"].strip()
        if len(text) > 30:   # ignore short filler speech
            important.append(clean_text(text))

    return " ".join(important)
