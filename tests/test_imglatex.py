#!/usr/bin/env python

"""Tests for `imglatex` package."""

import pytest

from click.testing import CliRunner

from imglatex import imglatex
from imglatex import cli


@pytest.mark.parametrize('path', [
    'something.png', 'somethingelse.jpg'
])
def test_supported_images(path):
    assert imglatex.is_supported(path)


@pytest.mark.parametrize('path', [
    'something.pdf', 'somethingelse.docx'
])
def test_not_supported_images(path):
    assert not imglatex.is_supported(path)


def test_grabbing_caption():
    image = imglatex.Image('something/the-image.png')
    assert image.caption == 'the image'


@pytest.mark.parametrize('img,should_float', [
    ('something/1.1the-image.png', True),
    ('something/the-image-no-identificada.png', False),
])
def test_should_float(img, should_float):
    image = imglatex.Image(img)
    assert image.should_float == should_float


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output
