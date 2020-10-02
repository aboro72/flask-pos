#!/bin/bash

# variables
MIGRATION_FILE=./migrations/env.py
DATABASE_FILE=./data-dev.sqlite
MIGRATION_FOLDER=./migrations
REQUIREMENT_FILE=./requirements.txt


# This entry is for a UserWarning: you have to edit the /etc/hosts and add a valid TLD to 127.0.0.1 or localhost
# But after that a valid certificate is needed (!?)
# CMD_RUN="flask run -h <domainname> -p 8000"

CMD_RUN="flask run -h localhost -p 8000"
CMD_INIT="flask db init"
CMD_TEST="flask test"
CMD_MIGRATE="flask db migrate"
CMD_UPGRADE="flask db upgrade"
CMD_CREATE_DB="flask createdb"

OPTIONS=":hpfqt"

export FLASK_ENV=development
export FLASK_CONFIG=development
export FLASK_APP=run.py

function help {
      echo "Help"
      echo "----"
      echo
      echo "./$(basename "$0") -f --> Force Recreate Migration Folder and Database"
      echo "./$(basename "$0") -p --> Install required Python Dependencies"
      echo "./$(basename "$0") -t --> Only run tests"
      echo "./$(basename "$0") -q --> Start PyQT Gui"
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

function start_gui {
    python3 Start.py
}

while getopts ${OPTIONS} arg; do
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
    q)
      echo
      start_gui
      exit 0
      ;;
    t)
      echo
      echo "Test Results:"
      echo "-------------"
      echo
      $CMD_TEST
      exit 0
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