import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """A Python CLI to backup all your GitHub repositories."""
    click.echo("Hello, world!")
