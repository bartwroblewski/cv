FROM python:3-alpine3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=views.py

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "20179","--reload"]