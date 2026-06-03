import typer

from doc_search.indexer import find_text_files

app = typer.Typer(
    help="Command-line tool that indexes and searches document collections."
)


@app.command()
def index(path: str):
    """Index a directory of documents."""
    files = find_text_files(path)

    print(f"Found {len(files)} text files.")

    for file in files:
        print(file)


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