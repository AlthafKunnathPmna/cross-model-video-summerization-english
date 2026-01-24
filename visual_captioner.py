import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(device)
model.eval()

def generate_captions(frame_dir, max_frames=6):
    captions = []
    frames = sorted(os.listdir(frame_dir))[:max_frames]

    for frame in frames:
        image = Image.open(
            os.path.join(frame_dir, frame)
        ).convert("RGB")

        inputs = processor(image, return_tensors="pt").to(device)

        with torch.no_grad():
            output = model.generate(**inputs, max_length=30)

        caption = processor.decode(
            output[0], skip_special_tokens=True
        )
        captions.append(caption)

    return captions
