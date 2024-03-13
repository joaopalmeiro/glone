from pathlib import Path

import click
import httpx
import trio
from gaveta.files import ensure_folder
from gaveta.time import ISOFormat, now_iso

from glone import __version__
from glone.cli.constants import (
    ARCHIVE_FORMAT,
    BASE_OUTPUT_FOLDER,
    BASE_URL,
    DEFAULT_ENV_VARIABLE,
    REPOS_ENDPOINT,
)
from glone.cli.models import Project, Projects


@click.command()
@click.option(
    "-t",
    "--token",
    type=str,
    metavar="VALUE",
    envvar=DEFAULT_ENV_VARIABLE,
    show_envvar=True,
)
@click.version_option(version=__version__)
def main(token: str) -> None:
    """A CLI to back up all your GitHub repositories."""
    output_folder = BASE_OUTPUT_FOLDER / now_iso(ISOFormat.BASIC)
    ensure_folder(output_folder)

    click.echo("Done!")
