FROM --platform=linux/amd64 python:3.9-slim-buster

ENV PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /web

ENTRYPOINT ["gunicorn"]
CMD ["web.wsgi:application", "-b", "0.0.0.0:8000", "--preload"]

# Install dependencies
RUN pip install -U poetry
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev

COPY . .

RUN python manage.py collectstatic --noinput --clear
