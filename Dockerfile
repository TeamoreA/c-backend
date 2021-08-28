FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

ENV FLASK_ENV=production

ENV GOOGLE_APPLICATION_CREDENTIALS=client_credentials.json

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]