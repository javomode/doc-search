import typer

app = typer.Typer(
    help="Command-line tool that indexes and searches document collections."
)


@app.command()
def index(path: str):
    """Index a directory of documents."""
    print(f"Indexing {path}")


@app.command()
def search(query: str):
    """Search indexed documents."""
    print(f"Searching for '{query}'")


@app.command()
def stats():
    """Show index statistics."""
    print("Showing statistics")


if __name__ == "__main__":
    app()