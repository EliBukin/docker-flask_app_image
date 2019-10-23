FROM ubuntu:18.04

RUN echo "my flask app"

COPY ./app /app

RUN apt update

RUN apt install python3-flask -y

ENV LC_ALL=C.UTF-8

ENV LANG=C.UTF-8

ENV FLASK_APP=/app/microblog.py
