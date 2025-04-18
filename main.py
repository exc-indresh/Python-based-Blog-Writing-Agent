import asyncio
import sys
from agents import context_agent, writing_agent, seo_agent, export_agent
from rich.console import Console
console = Console()

async def main(topic, tone="educational"):
    console.print(f"[bold yellow]🚀 Generating blog for topic: {topic}...")
    news, keywords = await asyncio.gather(
        context_agent.fetch_news_data(topic),
        context_agent.fetch_datamuse_keywords(topic),
    )

    if not keywords:
        console.print("[bold red]❌ Datamuse API returned unexpected content. Skipping keywords.")
        keywords = []

    outline = writing_agent.generate_outline(topic, tone)
    content = writing_agent.generate_section_content(topic, outline, tone)
    meta = seo_agent.generate_seo_metadata(topic, [k['word'] for k in keywords[:5]])
    export_agent.export_blog(topic, content, meta)

    console.print(f"[bold green]✅ Blog and metadata exported for topic: [italic]{topic}[/italic]")

if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else "AI in Healthcare"
    tone = sys.argv[2] if len(sys.argv) > 2 else "educational"
    asyncio.run(main(topic, tone))
