from pathlib import Path
from urllib.parse import urljoin

from platformdirs import user_documents_dir

DEFAULT_ENV_VARIABLE = "GITHUB_ACCESS_TOKEN"

BASE_URL = "https://api.github.com"
REPOS_ENDPOINT = "/user/repos"
REPOS_URL = urljoin(BASE_URL, REPOS_ENDPOINT)

BASE_OUTPUT_FOLDER = Path(user_documents_dir()) / "Backups" / "Repos" / "GitHub"
ARCHIVE_FORMAT = "zip"
