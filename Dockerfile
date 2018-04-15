FROM python:3.6.1-alpine

RUN apk update && apk add build-base
RUN pip install --upgrade pip

RUN mkdir /usr/src/app
WORKDIR /usr/src
COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1