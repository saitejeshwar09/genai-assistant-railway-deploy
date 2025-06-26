from fastapi import FastAPI, UploadFile, File, Form
from utils.parser import parse_document
from utils.summarizer import generate_summary
from utils.qa import answer_question
from utils.challenge import generate_questions, evaluate_answer

app = FastAPI()

doc_paragraphs = []

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global doc_paragraphs
    doc_paragraphs = parse_document(await file.read())
    return {"message": "File uploaded and parsed", "paragraph_count": len(doc_paragraphs)}

@app.get("/summary")
def get_summary():
    summary = generate_summary(doc_paragraphs)
    return {"summary": summary}

@app.get("/ask")
def ask_question(q: str):
    answer, _ = answer_question(q, doc_paragraphs)
    return {"question": q, "answer": answer}

@app.get("/challenge")
def challenge():
    return {"questions": generate_questions(doc_paragraphs)}

@app.post("/evaluate")
def evaluate(q: str = Form(...), a: str = Form(...)):
    result = evaluate_answer(a, q, doc_paragraphs)
    return {"correct": result}