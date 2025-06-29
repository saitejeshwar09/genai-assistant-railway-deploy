def generate_summary(paragraphs: list, max_len=3):
    if not paragraphs:
        return "No content to summarize."
    full_text = " ".join(paragraphs)
    sentences = full_text.split(". ")
    return ". ".join(sentences[:max_len]) + "."