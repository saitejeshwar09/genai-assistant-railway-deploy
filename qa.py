from utils.spacy_model import get_spacy_model
nlp = get_spacy_model()

def answer_question(question: str, paragraphs: list):
    if not paragraphs:
        return "No context found.", None

    context = " ".join(paragraphs)
    doc = nlp(context)
    similarities = [(sent.similarity(nlp(question)), sent.text) for sent in doc.sents]
    best = max(similarities, key=lambda x: x[0])
    return best[1], context.index(best[1]) if best[1] in context else None