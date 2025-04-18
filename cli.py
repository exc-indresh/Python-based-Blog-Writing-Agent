import click
from main import main
import asyncio

@click.command()
@click.argument("topic")
@click.option("--tone", default="educational", help="Tone of the blog (educational, technical, creative, etc.)")
def cli(topic, tone):
    asyncio.run(main(topic, tone))

if __name__ == "__main__":
    cli()
