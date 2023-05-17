#/usr/bin/env python
"""setup.py Installs FractalLab Python Library"""

__author__ = 'Jacob Taylor Cassady'
__email__ = 'jacobtaylorcassady@outlook.com'

from setuptools import setup, find_packages

MAJOR_VERSION: int = 0
MINOR_VERSION: int = 1
REVSION_VERSION: int = 0

if __name__ == '__main__':
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()

    setup(
        name='FractalLab',
        version=f'{MAJOR_VERSION}.{MINOR_VERSION}.{REVSION_VERSION}',
        author=__author__,
        author_email=__email__,
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/jtcass01/FractalLab',
        packages=find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: GNU General Public License :: V3',
            'Operating System :: OS Independent'
        ],
        python_requires='>=3.8'
    )
