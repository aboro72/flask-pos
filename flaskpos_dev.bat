@echo off
set MIGRATION_FILE="migrations\env.py"
set FLASK_APP=run.py
set FLASK_CONFIG=development
set FLASK_ENV=development

echo
echo "Flask-pos start script for development"
echo
echo "Init database if needed:"
IF EXIST %F% (
  @flask db upgrade
) ELSE (
  @flask db init
)
@flask createdb

echo
echo "Run tests:
@flask test
echo
echo "Start app:"
@flask run