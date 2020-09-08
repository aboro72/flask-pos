#!/bin/bash

MIGRATION_FILE=./migrations/env.py
export FLASK_ENV=development
export FLASK_CONFIG=development
export FLASK_APP=run.py

echo
echo "Flask-pos start script for development"
echo "--------------------------------------"
echo
echo "Init database if needed:"

if [ ! -f "$MIGRATION_FILE" ]; then
    flask db init
fi
flask db migrate
flask db upgrade
flask createdb

echo
echo "Run tests:"
flask test
echo
echo "Start app:"
flask run
