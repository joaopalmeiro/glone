from pathlib import Path

from platformdirs import user_documents_dir

DEFAULT_ENV_VARIABLE = "GITHUB_ACCESS_TOKEN"

BASE_URL = ""
REPOS_ENDPOINT = ""

BASE_OUTPUT_FOLDER = Path(user_documents_dir()) / "Backups" / "Repos" / "GitHub"
ARCHIVE_FORMAT = "zip"
