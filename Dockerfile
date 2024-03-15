FROM python:latest

RUN mkdir /automation

COPY . /automation

WORKDIR /automation

RUN pip install -r requirements.txt
