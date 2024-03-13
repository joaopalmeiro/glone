from pathlib import Path
from urllib.parse import urljoin

import click
import httpx
import trio
from gaveta.files import ensure_folder
from gaveta.time import ISOFormat, now_iso

from glone import __version__
from glone.cli.constants import (
    BASE_OUTPUT_FOLDER,
    BASE_URL,
    DEFAULT_ENV_VARIABLE,
    REPOS_ENDPOINT,
)
from glone.cli.models import Repos


def save_repos(repos: Repos, output_folder: Path) -> None:
    output_repos = output_folder / "repos.json"

    with output_repos.open(mode="w", encoding="utf-8") as f:
        f.write(repos.model_dump_json(indent=2))
        f.write("\n")

    click.echo(f"{output_repos} ✓")


async def get_repos(headers: httpx.Headers) -> Repos:
    repos = []
    next_url = urljoin(BASE_URL, REPOS_ENDPOINT)

    async with httpx.AsyncClient(
        headers=headers, params={"visibility": "all", "affiliation": "owner"}
    ) as client:
        while True:
            r = await client.get(next_url)

            data = r.json()
            repos.extend(data)

            try:
                next_url = r.links["next"]["url"]
            except KeyError:
                break

    return Repos(repos)


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

    headers = httpx.Headers(
        {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )
    repos = trio.run(get_repos, headers)
    save_repos(repos, output_folder)

    click.echo(f"Number of repos: {len(repos)}")
    click.echo(f"Output folder: {output_folder}")
    click.echo("Done!")
