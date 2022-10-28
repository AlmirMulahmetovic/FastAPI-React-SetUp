FROM python:3.9.15-bullseye as image

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv install --system --dev

COPY . /app/

CMD uvicorn app:app host=0.0.0.0 --reload