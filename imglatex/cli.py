"""Console script for imglatex."""

import click


@click.command()
def main(args=None):
    """Console script for imglatex."""
    click.echo("Replace this message by putting your code into "
               "imglatex.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
