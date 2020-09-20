@echo off

:: variables
set MIGRATION_FILE=migrations\env.py
set DATABASE_FILE=data-dev.sqlite
set MIGRATION_FOLDER=migrations

set CMD_RUN=flask run -h localhost -p 8000
set CMD_INIT=flask db init
set CMD_TEST=flask test
set CMD_MIGRATE=flask db migrate
set CMD_UPGRADE=flask db upgrade
set CMD_CREATE_DB=flask createdb

set FLASK_APP=run.py
set FLASK_CONFIG=development
set FLASK_ENV=development

echo -n ""
echo "Flask-pos start script for development"
if (%1 == "-f") (
  echo
  echo "Delete database & migration directory"
  IF EXIST %DATABASE_FILE% (
    @DEL /Q %DATABASE_FILE%
  )
  echo "."
  iF EXIST %MIGRATION_FOLDER% (
    @RD /S /Q %MIGRATION_FOLDER%
  )
  echo -n "."
)
echo -n ""
echo "Init database if needed:"
IF NOT EXIST %MIGRATION_FILE% (
  @%CMD_INIT%
)
@%CMD_MIGRATE%
@%CMD_UPGRADE%
@%CMD_CREATE_DB%

echo -n ""
echo "Run tests:
@%CMD_TEST%
echo -n ""
echo "Start app:"
@%CMD_RUN%
echo -n ""