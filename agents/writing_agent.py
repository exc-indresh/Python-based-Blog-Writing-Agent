import google.generativeai as genai
from core.config import GEMINI_API_KEY
from rich.console import Console
console = Console()
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def generate_outline(topic: str, tone: str = "educational") -> list[str]:
    prompt = f"""
    You are an expert blog writer. Generate an H2-level blog outline (5-6 sections)
    for a long-form blog on the topic: "{topic}". The tone should be {tone}.
    Only return the section titles.
    """
    response = model.generate_content(prompt)
    console.print("[bold cyan]✔ Outline generated.")
    return [line.strip("-• ") for line in response.text.split("\n") if line.strip()]

def generate_section_content(topic: str, outline: list[str], tone: str = "educational") -> str:
    markdown = f"# {topic}\n\n"

    # Intro
    intro_prompt = f"Write a short 150-word engaging introduction for a blog on: {topic}. Tone: {tone}"
    intro_resp = model.generate_content(intro_prompt)
    markdown += f"## Introduction\n\n{intro_resp.text.strip()}\n\n"

    for section in outline:
        prompt = f"Write 250 words for a blog section titled '{section}' under the topic '{topic}'. Tone: {tone}."
        resp = model.generate_content(prompt)
        markdown += f"## {section}\n\n{resp.text.strip()}\n\n"

    # Conclusion
    outro_prompt = f"Write a powerful conclusion for a blog on '{topic}', with a call to action. Tone: {tone}."
    outro_resp = model.generate_content(outro_prompt)
    markdown += f"## Conclusion\n\n{outro_resp.text.strip()}\n"

    console.print("[bold green]✔ Blog content fully generated.")
    return markdown
