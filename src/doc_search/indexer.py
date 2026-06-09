from pathlib import Path

from pypdf import PdfReader

# find text files
def find_text_files(root: str) -> list[Path]:
    return list(Path(root).rglob("*.txt"))

# find pdf files
def find_pdf_files(root: str) -> list[Path]:
    return list(Path(root).rglob("*.pdf"))


# read a text file
def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

# read a pdf file
def read_pdf_file(path: Path) -> str:
    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


# store document path, text based on file type as dict, later store each document in JSON
def create_document(path: Path) -> dict:
    if path.suffix.lower() == ".txt":
        text = read_text_file(path)

    elif path.suffix.lower() == ".pdf":
        text = read_pdf_file(path)

    else:
        text = ""

    return {
        "path": str(path),
        "text": text,
    }


# build index to compile document dict into single JSON
def build_index(root: str) -> list[dict]:
    txt_files = find_text_files(root)
    pdf_files = find_pdf_files(root)

    files = txt_files + pdf_files

    documents = []

    for file in files:
        documents.append(create_document(file))

    return documents
