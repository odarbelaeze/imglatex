"""Main module."""

import os

from jinja2 import Template


SUPPORTED_FORMATS = {'png', 'jpeg', 'jpg'}


def is_supported(path: str):
    """
    Figure out if a file is supported by extension.
    """
    name, extension = os.path.splitext(path)
    return extension.lower()[1:] in SUPPORTED_FORMATS


def find_images(path: str):
    """
    Finds the images in a folder.
    """
    for name in os.listdir(path):
        relative = os.path.join(path, name)
        if os.path.isfile(relative) and is_supported(relative):
            yield relative


class Image:
    def __init__(self, path: str):
        self.path = path
        self.caption = self._grab_caption(path)

    @staticmethod
    def _grab_caption(path: str):
        base = os.path.basename(path)
        name, _ = os.path.splitext(base)
        return name.replace('-', ' ')

    @property
    def should_float(self):
        """
        Should the image be rendered as a float or as just a
        standalone image.
        """
        return 'no identificada' not in self.caption

    @property
    def lyxpath(self):
        path, _ = os.path.splitext(self.path)
        return path.replace('.', '\lyxdot')

    @property
    def slug(self):
        return self.caption.replace(' ', '-').replace('.', '-')

    @property
    def template(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'templates/figure.tex'
        )
        with open(path) as inp:
            template_string = inp.read()
        return Template(template_string)

    @property
    def latex(self):
        return self.template.render(image=self)

    def __str__(self):
        return f'Image {self.caption}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.path})'


class Document:
    def __init__(self, images):
        self.images = images

    @property
    def template(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'templates/document.tex'
        )
        with open(path) as inp:
            template_string = inp.read()
        return Template(template_string)

    def latex(self):
        return self.template.render(images=self.images)
