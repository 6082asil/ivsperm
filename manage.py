#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ivs.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ivsperm.settings")
>>>>>>> 9226d2358e5e2f099a18e681b13334ebc842e9b3

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
