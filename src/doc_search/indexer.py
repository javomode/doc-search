from pathlib import Path


def find_text_files(root: str) -> list[Path]:
    return list(Path(root).rglob("*.txt"))
    # next add file traversal for pdf and user can choose txt, pdf, or both

# read a text file
def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

# store document path and text as dict, later store each document in JSON
def create_document(path: Path) -> dict:
    return {
        "path": str(path),
        "text": read_text_file(path),
    }

# build index to compile document dict into single JSON
def build_index(root: str) -> list[dict]:
    files = find_text_files(root)

    documents = []

    for file in files:
        documents.append(create_document(file))

    return documents