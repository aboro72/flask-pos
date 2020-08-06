# FLASK - POS

Administrate your Pos-System

### 1. Dependencies

- Flask               1.1.2
- Flask_SQLAlchemy    2.4.4

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

- [ Infos ](documentation/database/index.md "Database info" )
