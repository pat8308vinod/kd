FROM python:3.8-alpine

RUN apk update

RUN apk add --no-cache bash

COPY ./kdbackendapp /app

WORKDIR /app

COPY ./entrypoint.sh /


RUN apk add make automake gcc g++ subversion python3-dev

RUN apk add postgresql-dev 

RUN apk add musl-dev libffi-dev openssl-dev

RUN apk add curl dpkg

RUN apk add --no-cache jpeg-dev zlib-dev zlib

RUN apk add --no-cache --virtual .build-deps build-base linux-headers

RUN apk add cairo

RUN apk add cairo-dev pango-dev gdk-pixbuf

RUN apk add openssl-dev rust tcl-dev tiff-dev tk-dev

RUN apk add cargo freetype-dev gdk-pixbuf-dev \
    gettext jpeg-dev lcms2-dev  openjpeg-dev poppler-utils py-cffi

RUN apk update

RUN pip install --upgrade pip

COPY wait-for-it.sh .

RUN chmod +x /app/wait-for-it.sh

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# EXPOSE 8000

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kdbackendapp.wsgi:application"]


ENTRYPOINT ["sh","/entrypoint.sh"]