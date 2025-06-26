import random
from utils.qa import answer_question

def generate_questions(paragraphs: list, num=3):
    if not paragraphs:
        return []
    samples = random.sample(paragraphs, min(num, len(paragraphs)))
    return [f"What is discussed in: '{para[:60]}...?'" for para in samples]

def evaluate_answer(user_answer: str, question: str, paragraphs: list):
    correct_answer, _ = answer_question(question, paragraphs)
    return correct_answer.lower() in user_answer.lower()