#! /bin/bash

/wait-for-it.sh db:3306 -t 10
python3 manage.py makemigrations
python3 manage.py migrate
uwsgi --ini /code/.config/uwsgi.ini

