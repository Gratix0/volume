FROM python:3.10-slim

WORKDIR /app

COPY req.txt .
RUN pip install --no-cache-dir -r req.txt

COPY ./app ./app

WORKDIR /app
ENV SAVE_PATH="/data"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
