FROM python:3.12-alpine

WORKDIR /home/project/

COPY ./req.txt .

RUN pip install -r req.txt

COPY . . 