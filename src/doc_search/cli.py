import typer

from doc_search.indexer import build_index
from doc_search.search import get_snippet
from doc_search.storage import load_index, save_index

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
def search(query: str, snippet: bool = typer.Option(False, "--snippet", "-s")):
    """Search indexed documents."""
    try:
        documents = load_index()
    except FileNotFoundError:
        print("No index found.")
        print("Run: docsearch index <directory>")
        return

    for doc in documents:
        if query.lower() in doc["text"].lower():
            print(doc["path"])

            if snippet:
                print(get_snippet(doc["text"], query))


@app.command()
def stats():
    """Show index statistics."""
    try:
        documents = load_index()
    except FileNotFoundError:
        print("No index found.")
        print("Run: docsearch index <directory>")
        return
    document_count = len(documents)

    # number of document
    txt_count = 0
    pdf_count = 0

    for doc in documents:
        path = doc["path"].lower()

        if path.endswith(".txt"):
            txt_count += 1

        elif path.endswith(".pdf"):
            pdf_count += 1

    total_characters = 0

    # sum of characters
    for doc in documents:
        total_characters += len(doc["text"])

    # average document length
    if document_count > 0:
        average_length = total_characters / document_count
    else:
        average_length = 0

    print(f"Documents indexed: {document_count}")
    print(f"TXT files: {txt_count}")
    print(f"PDF files: {pdf_count}")
    print(f"Total characters indexed: {total_characters}")
    print(f"Average document length: {average_length:.0f} characters")


if __name__ == "__main__":
    app()
