import click
from ghapi.all import GhApi, paged

from . import __version__
from .constants import DEFAULT_ENV_VARIABLE


@click.command()
@click.argument("username", type=str)
@click.option(
    "-t",
    "--token",
    type=str,
    metavar="VALUE",
    envvar=DEFAULT_ENV_VARIABLE,
    show_envvar=True,
)
@click.version_option(version=__version__)
def main(username, token):
    """A Python CLI to backup all your GitHub repositories."""
    # More info:
    # - https://ghapi.fast.ai/core.html#GhApi
    # - https://ghapi.fast.ai/core.html#Operations
    # (if don't pass the token parameter, then your GITHUB_TOKEN environment variable
    # will be used, if available)
    # - https://ghapi.fast.ai/page.html#paged
    api = GhApi(owner=username, token=token)

    # More info:
    # - https://ghapi.fast.ai/fullapi.html#repos
    # - https://docs.github.com/en/rest/reference/repos#list-public-repositories
    # (it is not for a specific user)
    # - https://docs.github.com/en/rest/reference/repos#list-repositories-for-a-user
    # (public repositories)
    # - https://docs.github.com/en/rest/reference/repos#list-repositories-for-the-authenticated-user
    # (all repositories)

    # repos = api.repos.list_for_user(username=username, type="all", sort="pushed")
    repos = paged(
        api.repos.list_for_authenticated_user,
        visibility="all",
        affiliation="owner",
        sort="full_name",
    )

    for page in repos:
        # click.echo(len(page))
        for repo in page:
            click.echo(repo.name)
