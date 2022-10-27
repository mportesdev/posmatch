# coding: utf-8

from pathlib import Path
from setuptools import setup

import posmatch

long_description = Path('README.rst').read_text()

setup(
    name='posmatch',
    version=posmatch.__version__,
    author='Michal Porteš',
    author_email='michalportes1@gmail.com',
    description='Positional sub-pattern matching for custom classes.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/mportesdev/posmatch',
    license='MIT License',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['posmatch'],
    python_requires='>=3.9',
)
