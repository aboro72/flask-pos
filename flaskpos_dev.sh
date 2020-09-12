#!/bin/bash

# variables
MIGRATION_FILE=./migrations/env.py
DATABASE_FILE=./data-dev.sqlite
MIGRATION_FOLDER=./migrations
REQUIREMENT_FILE=./requirements.txt

CMD_RUN="flask run"
CMD_INIT="flask db init"
CMD_TEST="flask test"
CMD_MIGRATE="flask db migrate"
CMD_UPGRADE="flask db upgrade"
CMD_CREATE_DB="flask createdb"

optstring=":h:p"

export FLASK_ENV=development
export FLASK_CONFIG=development
export FLASK_APP=run.py

function help {
      echo "Help"
      echo "----"
      echo
      echo "./$(basename "$0") -f --> Force Recreate Migration Folder and Database"
      echo "./$(basename "$0") -p --> Install required Python Dependencies"
}

function recreate {
      echo "Delete database & migration directory"
      if [ -f "$DATABASE_FILE" ]; then
        rm $DATABASE_FILE
        echo "."
      fi

      if [ -d "$MIGRATION_FOLDER" ]; then
        rm -r $MIGRATION_FOLDER
        echo -n "."
      fi
}

function pipinstall {
      if [ ! -f "$REQUIREMENT_FILE" ]; then
        pip freeze > $REQUIREMENT_FILE
        echo
      fi
      if [ -f "$REQUIREMENT_FILE" ]; then
        pip install -r $REQUIREMENT_FILE
        echo
      fi
}

while getopts ${optstring} arg; do
  case ${arg} in
    h)
      echo
      help
      exit 0
      ;;
    f)
      echo
      recreate
      ;;
    p)
      echo
      pipinstall
      ;;
    ?)
      echo "Invalid option: -${OPTARG}."
      exit 1
      ;;
  esac
done


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