#!/bin/bash
set -e

find . -name '*.pyc' -delete
rm -fr media/*
rm -fr logs/*
rm -f db.sqlite3
python manage.py migrate --noinput
if [ "$1" != "--empty" ]; then
    python manage.py datacreator
fi
touch thirdfloor/settings.py
