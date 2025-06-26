FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN apt-get update &&     apt-get install -y gcc g++ build-essential &&     pip install --upgrade pip &&     pip install --no-cache-dir -r requirements.txt &&     python -m spacy download en_core_web_sm

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]