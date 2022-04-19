FROM node:16-bullseye-slim as angular

ENV NPM_CONFIG_AUDIT=false \
    NPM_CONFIG_FUND=false \
    NPM_CONFIG_UPDATE_NOTIFIER=false

WORKDIR /frontend/angular

# Install Node modules.
COPY ./web/frontend/angular/package*.json ./
RUN npm ci && npm cache clean --force

# Build the webpack bundle.
COPY ./web/frontend/angular/ ./
RUN npm run build -c production

# ------------------------------------------------------------------------------
FROM --platform=linux/amd64 python:3.9-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false \
    WEBPACK_STATS=/web/webpack-stats.json

WORKDIR /web

ENTRYPOINT ["python", "manage.py"]
CMD ["run"]

# Install dependencies.
RUN pip install -U poetry
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev

# Copy from host first so the files get overwritten by the next copy.
# The angular source files aren't needed, but it'd be tedious to
# exclude them; .dockerignore cannot be used for them since they are
# still needed by the first build stage.
COPY . .

# Copy the webpack bundle from the first stage.
# Can't copy the entire directory because .dockerignore doesn't get
# applied to individual copies between stages.
COPY --from=angular /frontend/static/ ./web/frontend/static/
COPY --from=angular /frontend/angular/webpack-stats.json $WEBPACK_STATS

# Set dummy value for env var so collectstatic can load settings.py.
RUN DATABASE_URL=postgres://localhost \
    python manage.py collectstatic --noinput --clear
