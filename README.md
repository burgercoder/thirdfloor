Third Floor
============

[![Build Status](https://travis-ci.org/burgercoder/thirdfloor.svg?branch=master)](https://travis-ci.org/burgercoder/thirdfloor)

Third Floor is the next generation doujinshi reader built with Django and Angular 2.

Name
----

- Third Floor
- 3F
- thirdfloor (code only)

Development Environment Setup
-----------------------------

Pre-requisites

- Python 3.5+

Install `virtualenv` and `virtualenvwrapper`

    pip install virtualenv virtualenvwrapper

Add the following to your `.bashrc` or `.bash_profile`

    export WORKON_HOME=~/.envs
    source /usr/local/bin/virtualenvwrapper.sh

Setup a Python virtual environment

    $ mkvirtualenv thirdfloor --python=/usr/bin/python3
    (thirdfloor) $

To reactivate the virtualenv in a new terminal window, use the `workon` command

    $ workon thirdfloor
    (thirdfloor) $

Install requirements and setup a local database

    (thirdfloor) $ ./scripts/upgrade.sh
    (thirdfloor) $ ./scripts/autosync.sh

Run the server

    (thirdfloor) $ python manage.py runserver
