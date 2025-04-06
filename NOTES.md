# Notes

- https://github.com/joaopalmeiro/template-python-cli
- EditorConfig:
  - https://github.com/github-linguist/linguist/blob/v7.28.0/lib/linguist/languages.yml#L1757
  - https://editorconfig.org/: "EditorConfig files use an INI format that is compatible with the format used by Python ConfigParser Library, but `[` and `]` are allowed in the section names."
- https://github.com/github-linguist/linguist/blob/v7.28.0/lib/linguist/languages.yml#L4033: `makefile`
- https://github.com/github-linguist/linguist/blob/v7.28.0/lib/linguist/languages.yml#L9:
  - `A String name of the Ace Mode used for highlighting whenever a file is edited. This must match one of the filenames in https://gh.io/acemodes. Use "text" if a mode does not exist.`
  - https://github.com/ajaxorg/ace/tree/master/src/mode
- https://github.com/github-linguist/linguist/blob/v7.28.0/lib/linguist/languages.yml#L7988: `yml` or `yaml`
- https://docs.github.com/rest:
  - https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28#authenticating-with-a-personal-access-token
  - https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repositories-for-the-authenticated-user
  - https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28#headers
  - https://docs.github.com/en/rest/about-the-rest-api/api-versions?apiVersion=2022-11-28#supported-api-versions
  - https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api?apiVersion=2022-11-28
  - https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#download-a-repository-archive-zip
- https://github.com/Colin-b/httpx_auth
- https://www.python-httpx.org/advanced/authentication/#custom-authentication-schemes
- https://gist.github.com/astrojuanlu/c5a416ab2a4abc9ae170b74177cc29d7
- https://www.python-httpx.org/async/#trio
- `paged()`
  - https://ghapi.fast.ai/page.html#paged
  - https://ghapi.fast.ai/page.html#link-header-rfc-5988
  - https://github.com/fastai/ghapi/blob/1.0.3/ghapi/page.py#L14
  - https://docs.python.org/3/library/itertools.html#itertools.takewhile
  - https://github.com/fastai/fastcore/blob/1.5.29/fastcore/imports.py#L35
- https://github.com/gidgethub/gidgethub
- https://github.com/encode/httpx/discussions/2662
- https://stackoverflow.com/questions/56248641/how-paginate-through-api-response-asynchronously-with-asyncio-and-aiohttp
- https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api?apiVersion=2022-11-28#scripting-with-pagination
- https://www.python-httpx.org/quickstart/#response-headers
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link
- https://github.com/encode/httpx/blob/0.27.0/httpx/_models.py#L782
- https://github.com/encode/httpx/blob/0.27.0/httpx/_models.py#L773
- https://github.com/octokit/octokit.js/issues/2369
- https://www.python-httpx.org/compatibility/#redirects:
  - "Unlike `requests`, HTTPX does **not follow redirects by default**."
  - `response = client.get(url, follow_redirects=True)`
  - `client = httpx.Client(follow_redirects=True)`
- https://stackoverflow.com/a/27472808: `echo "Today is $(date). A fine day."`
- https://ss64.com/mac/pbcopy.html
- https://www.encode.io/httpcore/async/#trio
- [Missing query params in url when params option is set](https://github.com/encode/httpx/issues/3433) issue:
  - "In version 0.28.0, query params are never merged."
  - https://github.com/encode/httpx/discussions/3428
  - https://github.com/encode/httpx/issues/3483
- [PoolTimeout when num tasks in asyncio.gather() exceeds client max_connections](https://github.com/encode/httpx/issues/1171) issue
- https://github.com/python-trio/trio/issues/527
- https://www.python-httpx.org/async/#streaming-responses: `async for chunk in response.aiter_bytes():`
- `timeout=60`
- https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28#about-secondary-rate-limits:
  - "Make too many concurrent requests. No more than 100 concurrent requests are allowed. This limit is shared across the REST API and GraphQL API."
- https://trio.readthedocs.io/en/stable/reference-core.html#trio.CapacityLimiter
  - https://www.python-httpx.org/advanced/resource-limits/: `max_keepalive_connections` is 20

## Snippets

```python
from pathlib import Path
from gaveta.json import write_json
write_json(repos, Path("repos.json"))
```

### `.github/dependabot.yml` file

```yml
# More info: https://docs.github.com/en/code-security/supply-chain-security/configuration-options-for-dependency-updates
version: 2
updates:
  # pip, pipenv, pip-compile, or poetry
  # More info: https://docs.github.com/en/code-security/supply-chain-security/about-dependabot-version-updates
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    # Disable version updates for pip dependencies
    open-pull-requests-limit: 0
```

### `.github/workflows/release.yml` file

```yml
# Source: https://cjolowicz.github.io/posts/hypermodern-python-06-ci-cd/

name: Release
on:
  release:
    types: [published]
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v1
        with:
          python-version: "3.6"
          architecture: x64
      - run: pip install poetry==1.1.11
      - run: poetry build
      - run: poetry publish --username=__token__ --password=${{ secrets.PYPI_TOKEN }}
```

### `.editorconfig` file

```ini
# More info: https://editorconfig.org/
# List of properties: https://github.com/editorconfig/editorconfig/wiki/EditorConfig-Properties
root = true

[*]
indent_style = space
indent_size = 4
insert_final_newline = true
trim_trailing_whitespace = true
end_of_line = lf
charset = utf-8

[*.{js,json,y{a,}ml,html}]
indent_style = space
indent_size = 2

[Makefile]
indent_style = tab

[*.{md,rst}]
trim_trailing_whitespace = false
indent_style = space
indent_size = 2
```

### `Makefile` file

```makefile
.PHONY: all check type isort black lint bandit

CMD:=poetry run
PYMODULE:=glone

all: check type isort black lint bandit

check:
	poetry check

type:
	$(CMD) mypy $(PYMODULE)

isort:
	$(CMD) isort $(PYMODULE)

black:
	$(CMD) black $(PYMODULE)

lint:
	$(CMD) flake8 $(PYMODULE)

bandit:
	$(CMD) bandit -r $(PYMODULE)
```

### `pyproject.toml` file (Poetry)

```toml
[tool.poetry]
name = "glone"
version = "0.1.0"
description = "A Python CLI to backup all your GitHub repositories."
authors = ["João Palmeiro <joaommpalmeiro@gmail.com>"]
license = "MIT"
readme = "README.md"
homepage = "https://github.com/joaopalmeiro/glone"
repository = "https://github.com/joaopalmeiro/glone"
keywords = ["glone", "cli", "backup", "repo", "repository", "github", "github-api"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Science/Research",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Terminals",
    "Topic :: Utilities"
]

[tool.poetry.urls]
"Bug Tracker" = "https://github.com/joaopalmeiro/glone/issues"
"Twitter" = "https://twitter.com/joaompalmeiro"

[tool.poetry.dependencies]
python = "^3.6"
importlib-metadata = {version = "^1.0", python = "<3.8"}
click = "^7.1.2"
ghapi = "^0.1.19"
fastcore = "^1.3.27"
humanize = "^3.13.1"

[tool.poetry.dev-dependencies]
mypy = "^0.812"
isort = "^5.7.0"
black = "^20.8b1"
flake8 = "^3.8.4"
bandit = "^1.7.0"
flake8-bugbear = "^21.3.1"
flake8-comprehensions = "^3.3.1"
pep8-naming = "^0.11.1"
flake8-builtins = "^1.5.3"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.scripts]
glone = "glone.cli:main"
```

### `README.md` file

```markdown
# glone

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python CLI to backup all your GitHub repositories.

## Development

- `poetry install`
- `poetry shell`

## Tech Stack

- [Click](https://click.palletsprojects.com/) (for the interface)

### Packaging and Development

- [Poetry](https://python-poetry.org/)
- [Mypy](http://mypy-lang.org/)
- [isort](https://pycqa.github.io/isort/)
- [Black](https://github.com/psf/black)
- [Flake8](https://flake8.pycqa.org/)
  - [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
  - [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)
  - [pep8-naming](https://github.com/PyCQA/pep8-naming)
  - [flake8-builtins](https://github.com/gforcada/flake8-builtins)
- [Bandit](https://bandit.readthedocs.io/)

This CLI was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`joaopalmeiro/cookiecutter-templates/python-cli`](https://github.com/joaopalmeiro/cookiecutter-templates) project template.

## Notes

- [Backup script](https://github.com/joaopalmeiro/scriptkit-playground/blob/main/google-zx/backup-gh.mjs).
- [ghapi documentation](https://ghapi.fast.ai/) ([API](https://ghapi.fast.ai/fullapi.html)).
- Commands:
  - `glone joaopalmeiro`.
  - `glone joaopalmeiro -o ~/Downloads`.
  - `glone joaopalmeiro -o ~/Downloads -f tar`.
  - `glone --help`.
  - `glone --version`.
- [GitPython](https://github.com/gitpython-developers/GitPython) package.
- [GitHub CLI](https://cli.github.com/) (a.k.a. `gh`).
- [humanize](https://github.com/jmoiron/humanize/) package. `poetry add humanize`.
```

### `glone/__init__.py` file

```python
import sys

if sys.version_info[:2] >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata

__version__ = importlib_metadata.version(__name__)
```

```python
async def get_single_archive(
    client: httpx.AsyncClient,
    repo: Repo,
    output_folder: Path,
    limiter: trio.CapacityLimiter,
) -> None:
    async with limiter:
        archive_url = generate_archive_endpoint(repo)
        filename = f"{repo.name}-{repo.default_branch}.{ARCHIVE_FORMAT}"
        output_archive = output_folder / filename

        r = await client.get(archive_url)

        async with await trio.open_file(output_archive, mode="wb") as f:
            # await f.write(r.content)
            # or
            async for chunk in r.aiter_bytes():
                await f.write(chunk)

        click.echo(f"{output_archive} ✓")
```

### `glone/cli.py` file

```python
from datetime import datetime
from pathlib import Path
from typing import Generator

import click
from fastcore.net import urlsend
from ghapi.all import GH_HOST, GhApi, paged
from humanize import naturalsize

from . import __version__
from .constants import (
    ARCHIVE_FILE_FORMATS,
    DEFAULT_ENV_VARIABLE,
    OUTPUT_FOLDER_PREFIX,
    OUTPUT_FOLDER_SEP,
)
from .utils import get_folder_file_count, get_folder_size


@click.command()
@click.argument("username", type=str)
@click.option(
    "-o",
    "--output",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, writable=True, resolve_path=True
    ),
    default=".",
    metavar="PATH",
    show_default=True,
)
@click.option(
    "-f",
    "--file-format",
    type=click.Choice(ARCHIVE_FILE_FORMATS, case_sensitive=False),
    default=ARCHIVE_FILE_FORMATS[0],
    show_default=True,
)
@click.option(
    "-t",
    "--token",
    type=str,
    metavar="VALUE",
    envvar=DEFAULT_ENV_VARIABLE,
    show_envvar=True,
)
@click.version_option(version=__version__)
def main(username: str, output: str, file_format: str, token: str) -> None:
    """A Python CLI to backup all your GitHub repositories."""
    # More info:
    # - https://ghapi.fast.ai/core.html#GhApi
    # - https://ghapi.fast.ai/core.html#Operations
    # (if don't pass the token parameter, then your GITHUB_TOKEN environment variable
    # will be used, if available)
    # - https://ghapi.fast.ai/page.html#paged
    api = GhApi(owner=username, token=token)
    # click.echo(api.headers)
    # click.echo(api.func_dict)

    # More info:
    # - https://ghapi.fast.ai/fullapi.html#repos
    # - https://docs.github.com/en/rest/reference/repos#list-public-repositories
    # (it is not for a specific user)
    # - https://docs.github.com/en/rest/reference/repos#list-repositories-for-a-user
    # (public repositories)
    # - https://docs.github.com/en/rest/reference/repos#list-repositories-for-the-authenticated-user
    # (all repositories)

    # repos = api.repos.list_for_user(username=username, type="all", sort="pushed")
    repos: Generator = paged(
        api.repos.list_for_authenticated_user,
        visibility="all",
        affiliation="owner",
        sort="full_name",
    )

    # More info:
    # - https://stackoverflow.com/a/50110841
    # - https://docs.python.org/3.6/library/pathlib.html#pathlib.Path.mkdir
    # - https://stackoverflow.com/a/32490661
    # - https://docs.python.org/3.6/library/pathlib.html#pathlib.Path.open
    timestamp: str = datetime.today().strftime(f"%Y%m%d{OUTPUT_FOLDER_SEP}%H%M%S")
    output_folder = (
        Path(output) / f"{OUTPUT_FOLDER_PREFIX}{OUTPUT_FOLDER_SEP}{timestamp}"
    )
    output_folder.mkdir(parents=False, exist_ok=False)

    click.echo(f"Output folder: {output_folder}")

    # More info:
    # - https://docs.github.com/en/rest/reference/repos#download-a-repository-archive-zip
    # - https://docs.github.com/en/rest/reference/repos#download-a-repository-archive-tar
    # - https://github.com/fastai/ghapi/issues/22
    # - https://github.com/fastai/fastcore/pull/308
    # - https://github.com/fastai/fastcore/blob/1.3.27/fastcore/net.py#L203
    # - https://stackoverflow.com/a/67964008
    # (ref="" for the master/main branch)
    # Note: It is not working. Use an alternative. See error message for debugging.
    # It would work if the execution was via this if branch, for example:
    # https://github.com/fastai/fastcore/blob/1.3.27/fastcore/net.py#L209
    # api.repos.download_zipball_archive(repo="glone", ref="")
    # api.repos.download_zipball_archive(repo="glone", ref="", archive_format="zip")

    # Workaround:
    # - https://fastcore.fast.ai/net.html#urlsend
    # - https://docs.github.com/en/rest/reference/actions#download-an-artifact
    # - https://docs.python.org/3.6/library/functions.html#open
    # - https://stackoverflow.com/a/6633693
    # - https://click.palletsprojects.com/en/7.x/options/?highlight=choice#choice-options
    # zip_url = (
    #     f"{GH_HOST}/repos/{username}/" + "{repo}/" + f"{file_format}ball" + "/{ref}"
    # )
    # route = {"repo": "glone", "ref": "", "archive_format": file_format}
    # or
    # route = {"repo": "glone", "ref": "", "archive_format": "zip"}

    # click.echo(zip_url)
    # click.echo(route)

    # res, headers = urlsend(
    #     zip_url, "GET", headers=api.headers, route=route, return_headers=True
    # )
    # click.echo(headers)

    # _, _, output_filename = headers["content-disposition"].partition("filename=")
    # click.echo(output_filename)
    # with open(output_folder / output_filename, "wb") as fh:
    #     fh.write(res)

    zip_url = (
        f"{GH_HOST}/repos/{username}/" + "{repo}/" + f"{file_format}ball" + "/{ref}"
    )
    for page in repos:
        # click.echo(len(page))
        for repo in page:
            click.echo(f"Repo: {repo.name}")

            route = {"repo": repo.name, "ref": "", "archive_format": file_format}
            res, headers = urlsend(
                zip_url, "GET", headers=api.headers, route=route, return_headers=True
            )

            _, _, output_filename = headers["content-disposition"].partition(
                "filename="
            )
            output_file_path = output_folder / output_filename

            with open(output_file_path, "wb") as fh:
                fh.write(res)

            click.echo(f"Archive file: {output_file_path}")
            # break
        # break

    click.echo(f"Number of archive files/repos: {get_folder_file_count(output_folder)}")
    # Compare with:
    # du -ch <OUTPUT_FOLDER>/*
    # du -sh <OUTPUT_FOLDER>
    size = get_folder_size(output_folder)
    click.echo(
        "Output folder size (approximate): "
        f"{naturalsize(size, binary=False, gnu=False)}"
    )

    click.echo("Done!")
```

### `glone/constants.py` file

```python
from typing import Tuple

DEFAULT_ENV_VARIABLE: str = "GITHUB_TOKEN"

# More info: https://en.wikipedia.org/wiki/ZIP_(file_format)
ARCHIVE_FILE_FORMATS: Tuple[str, str] = ("zip", "tar")

OUTPUT_FOLDER_PREFIX: str = "github"
OUTPUT_FOLDER_SEP: str = "-"
```

### `glone/utils.py` file

```python
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
```
