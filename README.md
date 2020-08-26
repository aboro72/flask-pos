# FLASK - POS

Administrate your Pos-System

### 1. Dependencies

The Dependencies are in the `requirements.txt`

if you want to exactly rebuild the development environment
run the following command:

    (venv) $ pip install -r requirements.txt
    
The required packages are outdated very quickly and you can try to use newer versions.
If you experience problems you can always go back and use the version specified here.

To generate your own requirements file use

    (venv) $ pip freeze >requirements.txt

### 2. Setup Development Environment

- Linux and Mac:

        $ export FLASK_APP=run.py
        $ export FLASK_CONFIG=development
        $ flask db init
        $ flask createdb
        $ flask run
- Windows cmd:

        > set FLASK_APP=run.py
        > set FLASK_CONFIG=development
        > flask db init
        > flask createdb
        > flask run
- Windows Powershell:

        > $env: FLASK_APP = "run.py"
        > $env: FLASK_CONFIG="development"
        > flask db init
        > flask createdb
        > flask run
- Setup Database\
To change Database add a environment variable
        
        Development: DEV_DATABASE_URL =
        Testing: TEST_DATABASE_URL =
        Production: DATABASE_URL=

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
    
    if you made some changes to the database use
    
        $ flask db upgrade
    

- Links:\
[ Database Tables ](documentation/database/index.md "Database Tables" )\
[ Flask-Migrate Website ](https://flask-migrate.readthedocs.io/en/latest/
                                                 "Online Documentation" )

### Test-User

If you use the command

    $ flask createdb
    
a user, employee and a role will be created for testing purposes

After that login is possible with:

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