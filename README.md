# Simple html to pdf converter api

## Set up application
0. For development purposes install `pipenv` (for system, not for current environment)
1. Install docker and docker-compose
2. Create `.env` file where you need to define variables like in env.example file:
3. Update `postgres.env` file and specify next variables(necessary for configuring docker container with postgres):
 - `POSTGRES_USER`
 - `POSTGRES_PASSWORD`
 - `POSTGRES_DB`

## local
1. Install wkhtmltopdf for mac `brew cask install wkhtmltopdf`
2. For activation env `pipenv shell`
2. Install packages `pipenv install`
 
 
## Docker
1. For activation env `pipenv shell`
Now you can use shortcuts:
 - `pipenv run db` - run container with DB
 - `pipenv run api` - run container with API

## How use 
endpoint http://localhost:8000/api/v1/convert/html POST request with body `link` or `file`