from pathlib import Path


def read_txt(filepath: Path | str):
    with open(filepath, "r") as file:
        return [row.strip() for row in file]
