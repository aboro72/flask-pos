# FLASK - POS

Administrate your Pos-System

### 1. Dependencies

- Flask             1.1.2
- Flask-Bootstrap   3.3.7.1
- Flask-Moment      0.10.0
- Flask-Migrate     2.5.3
- Flask-SQLAlchemy  2.4.4
- Flask-Login       0.5.0
- Flask-WTF         0.14.3

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

### Test-User

For the login a test-user was created with

    username: admin
    password: admin
    
for now it's only possible to Login / Logout but later on the line we will add some\
 more functionality like a profil maybe


### Unit-Tests

Because the app start & config needs some adjustments you need to set the environment-Variable to

    $ export FLASK_ENV = testing
    

Run Unit-Tests with
        
    $ flask test
        
At the moment unit-tests exists for:

- BASIC (is there an app / is the environment set to testing etc.)
- USER - Model (password is correct and is random)


### Planned:

Add / Change Permissions