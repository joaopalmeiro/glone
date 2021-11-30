from pathlib import Path


def get_folder_size(path: Path) -> int:
    # More info:
    # - https://docs.python.org/3.6/library/pathlib.html
    # - https://docs.python.org/3.6/library/pathlib.html#pathlib.Path.rglob
    # - https://docs.python.org/3.6/library/os.html#os.stat_result
    # - https://geekflare.com/check-file-folder-size-in-python/
    total_size = sum([f.stat().st_size for f in path.rglob("*")])
    return total_size


def get_folder_file_count(path: Path) -> int:
    # More info:
    # - https://www.kite.com/python/answers/how-to-count-the-number-of-files-in-a-directory-in-python
    # - https://docs.python.org/3.6/library/pathlib.html#pathlib.Path.iterdir
    # - https://docs.python.org/3.6/library/pathlib.html#pathlib.Path.is_file
    total_count = len([p for p in path.iterdir() if p.is_file()])
    return total_count
