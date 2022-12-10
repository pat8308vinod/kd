#!/bin/sh

gunicorn kdbackendapp.wsgi:application --bind 0.0.0.0:8000