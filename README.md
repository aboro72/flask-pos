# FLASK - POS

Administrate your Pos-System

### 1. Dependencies

- Flask             1.1.2
- Flask-Mail        0.9.1
- Flask-Migrate     2.5.3
- Flask-SQLAlchemy  2.4.4

### 2. Setup Development Environment

- Linux and Mac:

        $ export FLASK_APP=run.py
        $ export FLASK_ENV=development
        $ flask run
- Windows cmd:

        > set FLASK_APP=run.py
        > set FLASK_ENV=development
        > flask run
- Windows Powershell:

        > $env: FLASK_APP = "run.py"
        > $env: FLASK_ENV = "development"
        > flask run
- Setup Database\
To change Database add a environment variable
        
        DATABASE_URL=

    | Database | URL |
    |:---|:---|
    | Postgres | postgresql://username:password@hostname/database |
    | MySQL | mysql://username:password@hostname/database |
    | SQLite (Linux, MacOS) | sqlite:///absolute/path/to/database |
    | SQLite (Windows)  | sqlite:///c:/absolute/path/to/database

   
The Development Server will run at http://127.0.0.1:5000

### 3. Database

- Migration\
If the "migrations" folder doesn't exist, it has to be initialized with
       
       $ flask db init 
    To use automatic migration the following steps needs to be done
    + Make the necessary changes to the model classes
    + Create an automatic migration script with `$ flask db migrate`
    + Review the generated script and adjust it if needed
    + Add the migration script to source control
    + Apply the migration to the database with `$ flask db upgrade`
    
    if needed a migration message can be added, f.e.
    
        $ flask db migrate -m "initial migration"

- Links:\
[ Database Tables ](documentation/database/index.md "Database Tables" )\
[ Flask-Migrate Website ](https://flask-migrate.readthedocs.io/en/latest/
                                                 "Online Documentation" )
