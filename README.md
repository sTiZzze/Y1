## How to run

Create virtual env:

```
python -m venv .venv
```
Configure environment variables:

```
cp .env.sample .env


Fill out the .env file according to the example from .env.sample
```
Activate virtual env:

```
. .venv/Scripts/activate
```

Install dependencies (I use Python version 3.10 to run locally):

```
pip install -r requirements.txt
```
Start Postgres on Docker (Or if you want to use postgres locally, customize the .env for yourself and do not run Docker):


```
docker-compose up
```
Create a database with the name that you will use to configure POSTGRES_DB with .env

To apply alembic migrations:
```
alembic upgrade head
```

Start project:
```
uvicorn main:app --reload
```