FROM python:3.12-alpine

WORKDIR /home/project/

RUN apk add --update --no-cache gcc musl-dev postgresql-dev

COPY ./req.txt .

RUN pip install -r req.txt

COPY . .