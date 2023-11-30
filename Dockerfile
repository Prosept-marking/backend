FROM python:3.11-slim

WORKDIR /app

COPY Pipfile.lock Pipfile ./

RUN apt-get update && apt-get install -y gunicorn

RUN pip install pipenv

RUN pipenv install --deploy --ignore-pipfile

RUN pipenv install gunicorn

COPY . .

WORKDIR /app/backend

CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]
