# Blockchain Api App  


Blockchain Api app with flask,flask_restful,flask_jwt. 

#  Features!
  - python==3.6.2 
  - Flask==1.1.2
  - Flask-JWT-Extended==3.24.1
  - Flask-RESTful==0.3.8
  - Flask-SQLAlchemy==2.4.1
  - SQLAlchemy==1.3.16
  - passlib==1.7.2

### Installation

It requires  v3.7+ to run.
Clone project from github
```sh
$ git clone from the url
```
Install virtualenvironment...
```sh
$ pip3 install virtualenv
```
Create virtualenvironment...
```sh
$ virtualenv -p python3 venv
```
Activate environemnt...
```sh
$ source venv/bin/activate
```
Setup environemnt...
```sh
$ pip install -r requirements.txt
```

Run Project...
```sh
$ export FLASK_APP=run.py
$ flask run --port=8889
```


### Swagger Documentation URL
```sh
http://127.0.0.1:8889/api/v1/doc-ui/

http://127.0.0.1:8889/api/v1/doc/
```

## Docker update

### First create .env file with content

```shell
FLASK_APP=run.py
FLASK_DEBUG=True
FLASK_ENV=development
FLASK_RUN_PORT=8889
SECRET_KEY='3izb^ryglj(bvrjb2_y1fZvcnbky#358_l6-nn#i8fkug4mmz!'
JWT_SECRET_KEY='3izb^ryglj(bvrjb2_y1fZvcnbky#358_l6-nn#i8fkug4mmz!'
DEBUG=True
POSTGRES_DB=meta_athelete
POSTGRES_USER=meta_athelete
POSTGRES_PASSWORD=meta_athelete
DB_HOST=meta_postgres
```

All are example values. You can change values.

### Run docker

```shell
docker-compose up --build
```

### Database connection

After running docker, database manager will be exposed at: http://localhost:8890. Go there and give credentials:

```shell
System: PostgresSQL
Server: meta_postgres
Username: meta_athelete
Password: meta_athelete
Database: meta_athelete
```

From there you can import sql file.
