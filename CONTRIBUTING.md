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

```bash
poetry run python manage.py runserver
```

[poetry]: https://github.com/python-poetry/poetry/
