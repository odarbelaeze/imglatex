"""Console script for imglatex."""

import click

from imglatex.imglatex import find_images, Image, Document


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--prefix', default='.', help='Prefix for the image paths')
def main(path: click.Path, prefix: str):
    """Console script for imglatex."""
    document = Document(
        list(Image(i, prefix) for i in find_images(path))
    )
    click.echo(document.latex())
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
