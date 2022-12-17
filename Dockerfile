# syntax=docker/dockerfile:1

FROM python:3.11.1-slim-bullseye




RUN pip install --upgrade pip

COPY requirements.txt /requirements.txt


RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

ENTRYPOINT [ "python", "main.py"]
