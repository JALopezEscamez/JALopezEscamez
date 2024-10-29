# syntax= docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.11.8 as builder
EXPOSE 8000
WORKDIR /app

RUN apk update
RUN apk add \
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "manage.py", "runserver", "0.0.0.0:8000" ]