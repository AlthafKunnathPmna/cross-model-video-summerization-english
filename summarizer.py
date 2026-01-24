from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def generate_summary(transcript, ocr_text, visual_text):
    combined = f"""
TRANSCRIPT:
{transcript}

SLIDE TEXT:
{ocr_text}

VISUAL CONTEXT:
{visual_text}

Generate structured student notes with headings and bullet points.
"""

    summary = summarizer(
        combined,
        max_length=280,
        min_length=120,
        do_sample=False
    )

    return summary[0]["summary_text"]
