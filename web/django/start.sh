#!/bin/bash
# Start Gunicorn processes

echo Starting Gunicorn.
#exec /usr/local/bin/python manage.py migrate
#celery -A moonShot worker --loglevel=info
#/usr/local/bin/python manage.py migrate
exec gunicorn moonShot.wsgi:application --bind 0.0.0.0:8000 --workers 1