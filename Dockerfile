FROM python:3.6-alpine

RUN mkdir /app
WORKDIR /app

RUN apk add --update mariadb-dev
RUN apk add --no-cache \
            --virtual \
            .build-deps \
            python3-dev \
            build-base \
            linux-headers \
            gcc


COPY regalia/requirements/common.txt .
COPY regalia/requirements/production.txt .
RUN pip install -r production.txt

COPY . .

ENV NAME regalia