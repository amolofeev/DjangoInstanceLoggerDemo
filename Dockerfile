FROM python:alpine

COPY . /app

WORKDIR /app

RUN apk add git &&\
    pip install -r requirements.txt &&\
    apk del git

ENTRYPOINT ["/usr/local/bin/python", "manage.py", "runserver"]
