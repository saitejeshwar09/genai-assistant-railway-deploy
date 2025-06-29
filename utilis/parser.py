import fitz  # PyMuPDF

def parse_document(file_data) -> list:
    doc = fitz.open(stream=file_data, filetype="pdf")
    return [page.get_text().strip() for page in doc]