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
