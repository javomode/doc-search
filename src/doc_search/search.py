def get_snippet(text: str, query: str, context: int = 40) -> str:
    """
    Return text surrounding the first occurrence of query.
    """

    lower_text = text.lower()
    lower_query = query.lower()

    match_index = lower_text.find(lower_query)

    if match_index == -1:
        return ""

    start = max(0, match_index - context)
    end = min(len(text), match_index + len(query) + context)

    snippet = text[start:end]

    prefix = "..." if start > 0 else ""
    suffix = "..." if end < len(text) else ""

    return f"{prefix}{snippet}{suffix}"