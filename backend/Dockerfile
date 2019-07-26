FROM tiangolo/uwsgi-nginx:python3.6-alpine3.7

RUN apk upgrade --no-cache
RUN apk add --no-cache musl
RUN apk add --no-cache build-base
RUN apk add --no-cache postgresql-dev
RUN apk add --no-cache bash
RUN apk add --no-cache libffi-dev
RUN pip3 install --no-cache-dir --upgrade pip

COPY requirements.txt /

RUN cd / && pip3 install -r requirements.txt