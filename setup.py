#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'Jinja2>=2.10.1,<3',
    # TODO: Put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(odarbelaeze): Put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: Put package test requirements here
]

setup(
    name='imglatex',
    version='0.2.1',
    description="Turns a folder full of images into a LaTeX file that contains them as figures with captions.",
    long_description=readme + '\n\n' + history,
    author="Oscar Arbelaez",
    author_email='odarbelaeze@gmail.com',
    url='https://github.com/odarbelaeze/imglatex',
    packages=find_packages(include=['imglatex']),
    entry_points={
        'console_scripts': [
            'imglatex=imglatex.cli:main',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='imglatex',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
