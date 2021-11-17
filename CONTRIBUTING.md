# Development Environment

## Initial Setup

As prerequisites, Python 3.9, [npm], and [poetry] are required. Once those are installed, `cd` into the project's root directory and install the project's Python dependencies:

```bash
poetry install
```

Next, install the JavaScript dependencies:

```bash
cd web/frontend/angular
npm ci
cd ../../.. # go back to the root
```

Finally, install the pre-commit hook to ensure the linters will run upon a commit:

```bash
poetry run pre-commit install
```

## Running the Website

First create a `.env` file in the project's root directory and write the following to it:

```
DEBUG=true
```

Then, run the following command:

```bash
poetry run python manage.py run
```

This will host the server on http://127.0.0.1:8000 with Django in debug mode. It will automatically watch for changes, both to Angular and Django. For Angular, a rebuild of static files will be performed, but a browser page refresh will be required to see the changes.

### Alternative with Docker

Use Docker Compose (at least version `1.27.0`) to bring up the container. Note that with this method, installing Python and JS dependencies is not required, since it's all already done within the container.

```bash
docker-compose up
```

This will host the server on http://127.0.0.1:8000 with Django in debug mode. It will also mount the host machine's repository within the container. Therefore, changes made to local files on the host will be mirrored within the container. This avoids constant rebuilds after making changes. However, Angular static files will not automatically be rebuilt. Thus, this method is currently impractical for local development.

To forcefully rebuild the container, `--build` can be appended to the above command.

[npm]: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm/
[poetry]: https://github.com/python-poetry/poetry/
