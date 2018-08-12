FROM python:3.7.0-alpine3.7

RUN pip3 install telethon
RUN apk add --no-cache bash

COPY ./contents /contents