import click
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

# Initialize OpenAI client
client = OpenAI()
console = Console()

@click.command()
@click.argument('readme_path', type=click.Path(exists=True))
def readme_optimize(readme_path):
    """AI-powered README optimizer for clarity and completeness."""
    with open(readme_path, 'r') as f:
        readme_content = f.read()

    console.print(f"[bold blue]Optimizing README from {readme_path}...[/bold blue]")

    prompt = f"""
    Analyze the following README content and suggest improvements for clarity, completeness, structure, and SEO.
    Format your response in Markdown.

    README Content:
    {readme_content}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {{"role": "system", "content": "You are an expert technical writer and SEO specialist."}},
                {{"role": "user", "content": prompt}}
            ]
        )
        optimization_text = response.choices[0].message.content
        console.print(Markdown(optimization_text))
    except Exception as e:
        console.print(f"[bold red]Error during README optimization:[/bold red] {e}")

if __name__ == '__main__':
    readme_optimize()
