ARG APP_IMAGE=python:3.11-rc-alpine

FROM $APP_IMAGE as base

FROM base as builder

RUN mkdir /install

WORKDIR /install

COPY requirements.txt /requirements.txt


RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base



ADD . /project
WORKDIR /project

ENTRYPOINT [ "python", "main.py"]
