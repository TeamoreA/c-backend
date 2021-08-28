# FROM ubuntu:20.04

# RUN apt-get update -y && apt-get install -y python3-dev

# WORKDIR /app

# COPY . /app

# ENV FLASK_ENV production

# ENV GOOGLE_APPLICATION_CREDENTIALS cloudkite-interviews-timothy-51415fd2b4fa.json

# RUN pip3 --no-cache-dir install -r requirements.txt

# EXPOSE 5000

# ENTRYPOINT [ "python3" ]

# CMD [ "app.py" ]


FROM python:3.9

WORKDIR /app

COPY . /app

ENV FLASK_ENV production

ENV GOOGLE_APPLICATION_CREDENTIALS cloudkite-interviews-timothy-51415fd2b4fa.json

RUN pip3 --no-cache-dir install -r requirements.txt

# WORKDIR /c-backend

# COPY ./requirements.txt .

# RUN pip install -r requirements.txt

# ENV FLASK_ENV production

# COPY . .

# ENV GOOGLE_APPLICATION_CREDENTIALS cloudkite-interviews-timothy-51415fd2b4fa.json

# EXPOSE 5000