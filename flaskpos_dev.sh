export FLASK_ENV=development
export FLASK_CONFIG=development
export FLASK_APP=run.py

flask db-init
flask createdb
flask test
flask run
