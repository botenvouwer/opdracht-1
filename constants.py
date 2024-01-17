import os
from pathlib import Path

# Get the home folder of the current user
home_folder = Path(os.path.expanduser("~"))

FILE_PATH = home_folder / "Downloads"
