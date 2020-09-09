#!/bin/bash

# variables
MIGRATION_FILE=./migrations/env.py
DATABASE_FILE=./data-dev.sqlite
MIGRATION_FOLDER=./migrations

CMD_RUN="flask run"
CMD_INIT="flask db init"
CMD_TEST="flask test"
CMD_MIGRATE="flask db migrate"
CMD_UPGRADE="flask db upgrade"
CMD_CREATE_DB="flask createdb"

export FLASK_ENV=development
export FLASK_CONFIG=development
export FLASK_APP=run.py

echo
echo "Flask-pos start script for development"
echo "--------------------------------------"
if [[ "$1" == '-f' ]]; then
  echo
  echo "Delete database & migration directory"
  if [ -f "$DATABASE_FILE" ]; then
    rm $DATABASE_FILE
    echo "."
  fi

  if [ -d "$MIGRATION_FOLDER" ]; then
    rm -r $MIGRATION_FOLDER
    echo -n "."
  fi
fi
echo
echo "Init database if needed:"
if [ ! -f "$MIGRATION_FILE" ]; then
    $CMD_INIT
fi

$CMD_MIGRATE
$CMD_UPGRADE
$CMD_CREATE_DB

echo
echo "Run tests:"
$CMD_TEST
echo
echo "Start app:"
$CMD_RUN
echo
