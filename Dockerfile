FROM python:3.9

WORKDIR /c-backend

ENV FLASK_ENV=development

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "api/app.py" ]