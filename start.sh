#!/bin/bash

cd /opt/code/django_saltstack
python manage.py collectstatic
python manage.py syncdb --migrate
exec gunicorn --workers 5 --log-level=debug -b 0.0.0.0:8000 django_saltstack.wsgi:application
