import subprocess

def generate_notes(fused_content):
    prompt = f"""
Convert the following content into structured student notes.

Rules:
- Use headings
- Use bullet points
- Add Definitions section if applicable
- Add Key Takeaways

CONTENT:
{fused_content}
"""

    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()
