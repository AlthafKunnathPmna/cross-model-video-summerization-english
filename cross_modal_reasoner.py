import subprocess

def fuse_modalities(audio, visual, slides):
    prompt = f"""
You are an AI studying a lecture video.

AUDIO (spoken explanation):
{audio}

VISUAL (what is shown):
{visual}

SLIDES (on-screen text):
{slides}

TASK:
1. Keep only concepts supported by at least TWO modalities
2. Remove off-topic speech
3. Resolve contradictions
4. Organize information logically

Return clean structured content.
"""

    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()
