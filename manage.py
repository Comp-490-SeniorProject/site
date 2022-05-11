#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import shutil
import subprocess
import sys

# Must be set before settings are imported.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

try:
    import django
    from django.conf import settings
    from django.core.management import call_command, execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc


def prepare_server():
    """Apply migrations and collect static files."""
    print("Applying migrations.")
    call_command("migrate")

    if settings.DEBUG:
        print("Collecting static files.")
        call_command("collectstatic", interactive=False, clear=True, verbosity=0)


def run_ng_build():
    """Run the Angular build in watch mode and return its process handle."""
    print("Starting Angular build in watch mode.")

    node = shutil.which("node")
    if node is None:
        raise FileNotFoundError(
            "Cannot find the Node.js executable. "
            "Are you sure it's installed and available on your PATH environment variable?"
        )

    angular_root = (settings.BASE_DIR / "web" / "frontend" / "angular").resolve(strict=True)
    ng = angular_root / "node_modules" / "@angular" / "cli" / "bin" / "ng"

    try:
        ng.resolve(strict=True)
    except FileNotFoundError:
        raise FileNotFoundError(
            "Cannot find Angular CLI. Make sure you've installed the Node modules for Angular "
            f"by running 'npm ci' while in {angular_root}"
        )

    return subprocess.Popen(
        [node, str(ng), "build", "-c", "development", "--watch"],
        cwd=angular_root,
    )


def run_dev_server(cluster):
    """
    Simultaneously run the Django development server and ng build with --watch.

    `cluster` is the Django Q cluster to start concurrently with the server.
    """
    # Avoid spawning a new node node process every time Django reloads due to a file change.
    if os.environ.get("RUN_MAIN") != "true":
        node_process = run_ng_build()
    else:
        node_process = None

    try:
        # TODO: terminate runserver if ng build crashes?
        cluster.start()
        call_command("runserver", "0.0.0.0:8000")
    finally:
        cluster.stop()
        if node_process:
            node_process.terminate()


def run_server():
    """Prepare and run the web server."""
    django.setup()  # This must only be called once.

    # `RUN_MAIN` is set to None the first time `runserver` is called. When the `use_reloader` option
    # is set (it is set by default), `RUN_MAIN` is set to "true" upon a reload after a code change.
    # To avoid preparing twice at the start, only prepare when in the reloader. Since `runserver`
    # is only using during debug mode, the `RUN_MAIN` check only needs to happen in debug mode.
    if not settings.DEBUG or os.environ.get("RUN_MAIN") == "true":
        prepare_server()

    print("Starting server.")

    # The cluster is responsible for executing scheduled tasks.
    from django_q.cluster import Cluster

    cluster = Cluster()

    if settings.DEBUG:
        run_dev_server(cluster)
    else:
        import gunicorn.app.wsgiapp

        # Patch the arguments for gunicorn.
        sys.argv = [
            "gunicorn",
            "web.wsgi:application",
            "-b",
            "0.0.0.0:8000",
            "--access-logfile",
            "-",
            "--error-logfile",
            "-",
            "--preload",
        ]

        try:
            cluster.start()
            gunicorn.app.wsgiapp.run()
        finally:
            cluster.stop()


def main():
    """Run administrative tasks."""
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        run_server()
    else:
        execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
