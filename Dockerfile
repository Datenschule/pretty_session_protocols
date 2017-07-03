FROM python:3.6.1-alpine

# Required for psycopg2
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "views.py"]