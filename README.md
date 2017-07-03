# Pretty session protocols

## Installation
```bash
pip install -r requirement.txt
```

## Running:

```bash
DATABSE_URL=<db_url> python views.py
#e.g.: DATABSE_URL=sqlite:////home/user/db.sqlite python views.py
```

## Docker 
You can run this project with docker compose. It will create a instance for the database and one for the actual app.
```bash
docker-compose up
```
The postgres data will be stored in the local `plpr-docker-database-data` folder. 

You can access the webapp by visiting http://localhost:8090. The database listens locally on port 32780.