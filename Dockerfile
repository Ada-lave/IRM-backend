FROM python:3.12-alpine

WORKDIR /home/ada/project/
COPY . .

RUN pip install -r req.txt

WORKDIR /home/ada/project/irm_backend

RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000