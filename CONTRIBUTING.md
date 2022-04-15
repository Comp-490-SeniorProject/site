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

### AWS

AWS credentials are required to use the AWS SDK. An access key ID and a secret access key are needed. To acquire these credentials, see the _To manage access keys when signed in as an IAM user_ section [here](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html).

Create a `.env` file in the project's root directory and write the following to it:

```
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_DEFAULT_REGION=us-west-1
```

Replace the first two values with the generated credentials.

## Running the Website

The site relies on a PostgreSQL-specific feature (array columns). While it is possible to set up a PostgreSQL instance manually, it is out of scope for this guide. Instead, it will show how to set up PostgreSQL through Docker Compose. However, it will show how to run the web server either outside or inside Docker. Note that in both cases, at least Docker Compose version `1.27.0` is required.

### Web Server Outside Docker

Running the web server without Docker has two main advantages: it's potentially easier to attach a debugger and Angular can automatically rebuild static files upon detecting changes.

Add the following lines to the `.env` file created earlier:

```
DATABASE_URL=postgres://admin:pass@127.0.0.1:7000/web
DEBUG=true
```

Then, run the following commands. Give the database around 15 seconds to become ready before running the second command.

```bash
docker-compose up -d db
poetry run python manage.py run
```

This will host the server on http://127.0.0.1:8000 with Django in debug mode. It will automatically watch for changes, both to Angular and Django. For Angular, a rebuild of static files will be performed, but a browser page refresh will be required to see the changes.

To stop the web server, use <kbd>Ctrl</kbd> + <kbd>c</kbd> in the terminal (<kbd>Ctrl</kbd> + <kbd>Break</kbd> on Windows). To stop the database, use `docker-compose down`.

### Web Server Inside Docker

Use Docker Compose to bring up the container. Note that with this method, installing Python and JS dependencies is not required, since it's all already done within the container.

```bash
docker-compose up
```

This will host the server on http://127.0.0.1:8000 with Django in debug mode. It will also mount the host machine's repository within the container. Therefore, changes made to local files on the host will be mirrored within the container. This avoids constant rebuilds after making changes. However, Angular static files will not automatically be rebuilt. Thus, this method is currently impractical for local development.

To forcefully rebuild the container, `--build` can be appended to the above command. To stop the services, use <kbd>Ctrl</kbd> + <kbd>c</kbd> in the terminal.

[npm]: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm/
[poetry]: https://github.com/python-poetry/poetry/
