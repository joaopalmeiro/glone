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
