FROM python:3.9.15-bullseye as image

WORKDIR /server

COPY Pipfile Pipfile.lock /server/

RUN pip install pipenv && pipenv install --system --dev

COPY . /server/

CMD uvicorn app:app host=0.0.0.0 --reload