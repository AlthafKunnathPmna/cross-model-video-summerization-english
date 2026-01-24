import subprocess

def refine_visual_context(captions):
    if not captions:
        return "No significant visual content detected."

    prompt = f"""
You are analyzing educational video frames.

Raw visual descriptions:
{chr(10).join('- ' + c for c in captions)}

Instructions:
- Merge similar ideas
- Explain visuals clearly for student notes
- Focus on concepts, diagrams, and teaching material
- Be concise

Return a clean explanation.
"""

    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()
