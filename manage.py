#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import shutil
import subprocess
import sys

try:
    import django
    from django.core.management import call_command, execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc


def run_dev_server():
    """Simultaneously run the Django development server and ng build with --watch."""
    # Must be imported only after DJANGO_SETTINGS_MODULE is set.
    from django.conf import settings

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

    node_process = subprocess.Popen(
        [node, str(ng), "build", "-c", "development", "--watch"],
        cwd=angular_root,
    )

    try:
        # TODO: terminate runserver if ng build crashes?
        django.setup()
        call_command("runserver", "0.0.0.0:8000")
    except Exception:
        # If Django fails, terminate Angular's build too.
        node_process.terminate()
        raise
    else:
        # Wait for the process so that signals are forwarded if this wait is interrupted.
        # In practice, this may be unreachable since Django won't stop unless an exception happens.
        node_process.wait()


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

    if len(sys.argv) > 1 and sys.argv[1] == "run":
        run_dev_server()
    else:
        execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
