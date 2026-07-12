FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    espeak-ng \
    sox \
    libsox-fmt-all \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN mkdir -p /app/audios

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
