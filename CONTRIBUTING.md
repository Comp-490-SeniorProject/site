# Development Environment

## Initial Setup

As prerequisites, Python 3.9 and [poetry] are required. Once those are installed, `cd` into the project's root directory and install the project's Python dependencies:

```bash
poetry install
```

Finally, install the pre-commit hook to ensure the linters will run upon a commit:

```bash
poetry run pre-commit install
```

## Running the Website

Use Docker Compose to bring up the container.

```bash
docker-compose up
```

This will host the server on http://127.0.0.1:8000 with Django in debug mode. It will also mount the host machine's repository within the container. Therefore, changes made to local files on the host will be mirrored within the container. This avoids constant rebuilds after making changes.

To forcefully rebuild the container, `--build` can be appended to the above command.

### Alternative to Docker

To run the site without Docker, first create a `.env` file in the project's root directory and write the following to it:

```
DEBUG=true
```

Then, run the following command:

```bash
poetry run python manage.py runserver
```

[poetry]: https://github.com/python-poetry/poetry/
