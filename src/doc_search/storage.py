import json

# store documents found and read from indexer.py as JSON
def save_index(documents, output_file="index.json"):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2)

# return current JSON
def load_index(index_file="index.json"):
    with open(index_file, "r", encoding="utf-8") as f:
        return json.load(f)