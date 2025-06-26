FROM python:3.9-slim

WORKDIR /app

# Update packages and install system build tools
RUN apt-get update && \
    apt-get install -y gcc g++ build-essential

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# (Optional: skip this if your requirements already include the model)
# RUN python -m spacy download en_core_web_sm

# Copy all app files
COPY . .

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
