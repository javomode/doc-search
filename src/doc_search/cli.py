import typer

from doc_search.indexer import build_index
from doc_search.storage import save_index, load_index

app = typer.Typer(
    help="Command-line tool that indexes and searches document collections."
)

# next add file traversal for pdf and user can choose txt, pdf, or both
@app.command()
def index(path: str):
    """Index a directory of documents."""
    documents = build_index(path)

    save_index(documents)

    print(f"Indexed {len(documents)} documents.")


@app.command()
def search(query: str):
    """Search indexed documents."""
    documents = load_index()

    for doc in documents:
        if query.lower() in doc["text"].lower():
            print(doc["path"])


@app.command()
def stats():
    """Show index statistics."""
    print("Showing statistics")


if __name__ == "__main__":
    app()