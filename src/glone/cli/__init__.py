from pathlib import Path

import click
import httpx
import trio
from gaveta.files import ensure_dir
from gaveta.time import ISOFormat, now_iso

from glone import __version__
from glone.cli.constants import (
    ARCHIVE_FORMAT,
    BASE_OUTPUT_FOLDER,
    BASE_URL,
    DEFAULT_ENV_VARIABLE,
    REPOS_URL,
)
from glone.cli.models import Repo, Repos


def save_repos(repos: list[Repo], output_folder: Path) -> None:
    output_repos = output_folder / "repos.json"

    with output_repos.open(mode="w", encoding="utf-8") as f:
        f.write(Repos.dump_json(repos, indent=2).decode("utf-8"))
        f.write("\n")

    click.echo(f"{output_repos} ✓")


async def get_repos(headers: httpx.Headers) -> list[Repo]:
    repos = []
    next_url = httpx.URL(
        REPOS_URL, params={"visibility": "all", "affiliation": "owner"}
    )

    async with httpx.AsyncClient(headers=headers) as client:
        while True:
            r = await client.get(next_url)

            data = r.json()
            repos.extend(data)

            try:
                next_url = httpx.URL(r.links["next"]["url"])
            except KeyError:
                break

    return Repos.validate_python(repos)


def generate_archive_endpoint(repo: Repo) -> str:
    return f"/repos/{repo.full_name}/{ARCHIVE_FORMAT}ball/{repo.default_branch}"


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
            async for chunk in r.aiter_bytes():
                await f.write(chunk)

        click.echo(f"{output_archive} ✓")


async def get_archives(
    headers: httpx.Headers, repos: list[Repo], output_folder: Path
) -> None:
    limiter = trio.CapacityLimiter(20)

    async with (
        httpx.AsyncClient(
            base_url=BASE_URL, headers=headers, follow_redirects=True
        ) as client,
        trio.open_nursery() as nursery,
    ):
        for repo in repos:
            nursery.start_soon(get_single_archive, client, repo, output_folder, limiter)


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
    ensure_dir(output_folder)

    headers = httpx.Headers(
        {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )

    repos = trio.run(get_repos, headers)
    save_repos(repos, output_folder)

    trio.run(get_archives, headers, repos, output_folder)

    click.echo(f"Number of repos: {len(repos)}")
    click.echo(f"Output folder: {output_folder}")
    click.echo("Done!")
