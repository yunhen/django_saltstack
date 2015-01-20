#!/bin/bash

cd /opt/code/django_saltstack
python manage.py collectstatic --noinput
python manage.py syncdb --migrate --noinput
exec gunicorn --workers 5 --log-level=debug -b 0.0.0.0:8000 django_saltstack.wsgi:application
