@echo off
set FLASK_APP=run.py
set FLASK_CONFIG=development
set FLASK_ENV=development

@flask db init
@flask createdb
@flask test
@flask run