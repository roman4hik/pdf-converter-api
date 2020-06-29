#!/bin/bash
set -e

cd $PROJECT_PATH
python manage.py migrate

#echo "Starting test Server!"
python manage.py runserver 0.0.0.0:8000
