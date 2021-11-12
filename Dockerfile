FROM node:16-bullseye-slim as angular

WORKDIR /frontend/angular

# Install Node modules.
COPY ./web/frontend/angular/package*.json ./
RUN npm ci

# Build the webpack bundle.
COPY ./web/frontend/angular/ ./
RUN npm run build -c production

FROM --platform=linux/amd64 python:3.9-slim-bullseye

ENV PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /web

ENTRYPOINT ["gunicorn"]
CMD ["web.wsgi:application", "-b", "0.0.0.0:8000", "--preload"]

# Install dependencies.
RUN pip install -U poetry
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev

# Copy the bundle from the previous step and copy the rest of the source files.
# The Angular source files aren't needed, but it's not worth the hassle to
# delete them.
COPY --from=angular /frontend/ ./frontend/
COPY . .

# Set dummy value for env var so collectstatic can load settings.py.
RUN DATABASE_URL=postgres://localhost \
    python manage.py collectstatic --noinput --clear
