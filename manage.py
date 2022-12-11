#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import pymongo

from djangoProject.utils import get_db_handle


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
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

    db_client, current_db = get_db_handle("yourchancedb")
    collection = current_db["projects"]

    document = {
        'name': 'MyProject'
    }
    result = collection.insert_one(document)
    print(result.inserted_id)
