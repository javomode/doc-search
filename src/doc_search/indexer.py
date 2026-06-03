from pathlib import Path


def find_text_files(root: str) -> list[Path]:
    return list(Path(root).rglob("*.txt"))