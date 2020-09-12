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

    - run script: `flaskpos_dev.sh`
        - command `-f`\
            new database\
            recreate migrations folder
        - command `-p`\
            install Python dependencies
    
    - if you want to run it manually:

            $ export FLASK_APP=run.py
            $ export FLASK_CONFIG=development
            $ export FLASK_ENV=development
            $ flask db init
            $ flask createdb
            $ flask run
- Windows cmd:

    - run script: `flaskpos_dev.bat`\
      - command `-f`\
        new database\
        recreate migrations folder
    
    - if you want to run it manually:

            > set FLASK_APP=run.py
            > set FLASK_CONFIG=development
            > set FLASK_ENV=development
            > flask db init
            > flask createdb
            > flask run
- Windows Powershell:

        > $env: FLASK_APP = "run.py"
        > $env: FLASK_CONFIG="development"
        > $env: FLASK_ENV="development"
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
    
for testing purposes the following roles will be created
if you run `flask createdb`

- Admin Account:

        username: admin
        password: admin

- Owner Account:

        username: owner
        password: owner

- Manager Account:

        username: manager
        password: manager

- User Account:

        username: user
        password: user
           
But it's possible to view, create, edit and delete users.

the created user will have `0000` as password and is not activated.
Currently it is not possible to change the password. It will be implemented later.

### Unit-Tests

Because the app start & config needs some adjustments you need to set the environment-Variable to

    $ export FLASK_ENV = testing
    

Run Unit-Tests with
        
    $ flask test
        
Test-Dictionary:

- BASIC (is there an app / is the environment set to testing etc.)
- USER MODEL (password is correct and salt is random)
- ROLE MODEL (Permissions are correct)


### Planned:

add time - control 