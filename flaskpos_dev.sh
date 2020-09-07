export FLASK_ENV=development
export FLASK_CONFIG=development
export FLASK_APP=run.py

flask createdb
flask run
