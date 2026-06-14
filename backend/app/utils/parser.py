import json
import yaml


def parse_file(file_path):

    extension = file_path.split(".")[-1].lower()

    if extension == "json":
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    elif extension in ["yaml", "yml"]:
        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    else:
        raise ValueError("Unsupported file type")