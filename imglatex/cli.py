"""Console script for imglatex."""

import click

from imglatex.imglatex import find_images, Image


@click.command()
@click.argument('path', type=click.Path(exists=True))
def main(path: click.Path):
    """Console script for imglatex."""
    click.echo("Replace this message by putting your code into "
               "imglatex.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    click.echo('\n'.join(str(Image(i)) for i in find_images(path)))
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
