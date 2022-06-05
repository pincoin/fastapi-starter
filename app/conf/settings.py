import json
import os

from . import PROJECT_DIR

with open(os.path.join(PROJECT_DIR, "secret.json"), "r") as file:
    settings = json.load(file)
