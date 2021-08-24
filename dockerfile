# syntax=docker/dockerfile:1

FROM python:3.9.6-bullseye

WORKDIR /meeting_planner

COPY . /meeting_planner/

RUN pip install -r requirements.txt 

# RUN python manage.py migrate

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]
