import typer

from doc_search.indexer import build_index, read_text_file
from doc_search.storage import load_index, save_index
from doc_search.search import get_snippet

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
def search(
    query: str,
    snippet: bool = typer.Option(False, "--snippet", "-s")
):
    """Search indexed documents."""
    documents = load_index()

    for doc in documents:
        if query.lower() in doc["text"].lower():
            print(doc["path"])

            if snippet:
                print(get_snippet(doc["text"], query))


@app.command()
def stats():
    """Show index statistics."""
    print("Showing statistics")


if __name__ == "__main__":
    app()
