FROM python:3.12.0-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY sentiment_analysis.py .

CMD ["python", "sentiment_analysis.py"]