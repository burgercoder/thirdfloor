#!/bin/sh
set -e
mypy --strict-optional --disallow-untyped-defs --disallow-untyped-calls --silent-imports thirdfloor
pylint thirdfloor
python manage.py test
