#!/bin/bash

echo "Applying migrations(assuming database is ready to go)"
python3 manage.py migrate

python3 manage.py collectstatic --no-input

gunicorn --workers 3 --bind 0.0.0.0:8000 xtracker.wsgi