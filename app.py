import streamlit as st
import os
import tempfile

from video_processor import extract_frames, extract_audio
from audio_to_text import extract_important_audio
from visual_captioner import generate_captions
from ollama_reasoner import refine_visual_context
from ocr_extractor import extract_slide_logic
from cross_modal_reasoner import fuse_modalities
from notes_generator import generate_notes

st.set_page_config(page_title="Cross-Modal Video Notes AI")
st.title("🎓 Cross-Modal Video Notes Generator")

video = st.file_uploader("Upload Lecture Video", type=["mp4", "mkv", "avi"])

if video:
    os.makedirs("temp", exist_ok=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(video.read())
        video_path = tmp.name
    with open(video_path, "wb") as f:
        f.write(video.read())

    with st.spinner("Extracting content..."):
        extract_frames(video_path)
        extract_audio(video_path)

    with st.spinner("Understanding audio..."):
        audio_text = extract_important_audio("temp/audio.wav")

    with st.spinner("Understanding visuals..."):
        captions = generate_captions("temp/frames")
        visual_text = refine_visual_context(captions)

    with st.spinner("Reading slides..."):
        slide_text = extract_slide_logic("temp/frames")

    with st.spinner("Fusing modalities..."):
        fused = fuse_modalities(audio_text, visual_text, slide_text)

    with st.spinner("Generating notes..."):
        notes = generate_notes(fused)

    st.subheader("📘 Generated Study Notes")
    st.write(notes)

    st.download_button(
    label="⬇️ Download Notes (Markdown)",
    data=notes,
    file_name="video_notes.md",
    mime="text/markdown")

