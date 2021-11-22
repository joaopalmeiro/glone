import click
from fastcore.net import urlsend
from ghapi.all import GH_HOST, GhApi, paged

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
    repos = paged(
        api.repos.list_for_authenticated_user,
        visibility="all",
        affiliation="owner",
        sort="full_name",
    )

    # More info:
    # - https://docs.github.com/en/rest/reference/repos#download-a-repository-archive-zip
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
    # - https://fastcore.fast.ai/net.html#urlsend)
    # - https://docs.github.com/en/rest/reference/actions#download-an-artifact
    # - https://docs.python.org/3.6/library/functions.html#open
    # - https://stackoverflow.com/a/6633693
    zip_url = f"{GH_HOST}/repos/{username}/" + "{repo}/zipball/{ref}"
    route = {"repo": "glone", "ref": "", "archive_format": "zip"}
    # click.echo(zip_url, route)

    res, headers = urlsend(
        zip_url, "GET", headers=api.headers, route=route, return_headers=True
    )
    # click.echo(headers)

    _, _, output_filename = headers["content-disposition"].partition("filename=")
    # click.echo(output_filename)
    with open(output_filename, "wb") as fh:
        fh.write(res)

    # for page in repos:
    #     # click.echo(len(page))
    #     for repo in page:
    #         click.echo(repo.name)
