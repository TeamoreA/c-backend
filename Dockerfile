FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

ENV FLASK_ENV production

ENV GOOGLE_APPLICATION_CREDENTIALS cloudkite-interviews-timothy-51415fd2b4fa.json

RUN pip3 --no-cache-dir install -r requirements.txt