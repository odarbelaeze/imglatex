"""Main module."""

import os


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

    def __str__(self):
        return f'Image {self.caption}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.path})'
