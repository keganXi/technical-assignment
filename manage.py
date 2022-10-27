#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

    # if GITHUB_WORKFLOW environment variable exists
    # assign ci.py settings file path to DJANGO_SETTINGS_MODULE
    # environment variable, if not assign development.py file path.   
    settings = "technical_assignment.settings.development"
    if os.environ.get('GITHUB_WORKFLOW'):
        settings = "technical_assignment.settings.ci"

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
