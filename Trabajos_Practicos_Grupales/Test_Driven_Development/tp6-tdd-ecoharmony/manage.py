import os
import sys
from pathlib import Path
from django.core.management import execute_from_command_line

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecoharmony.settings")
    execute_from_command_line(sys.argv)
