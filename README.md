## Dotenv example:
```dotenv
NAME=postgres
USER=postgres
PASSWORD=postgres
HOST=db
PORT=5432
```

## Quickstart:
```bash
pip install -r requirements.txt
```
```bash
python tasks/manage.py runserver
```
go to http://localhost:8000/tasks or http://localhost:8000/performers

## Running with docker:
```bash
docker compose up --build
```
