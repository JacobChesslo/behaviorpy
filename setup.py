#!/usr/bin/env python
"""BehaviorPy: Behavior-Analysis Library for Python

BehaviorPy is an open-source software for the behavioral sciences.
"""


def setup():
    from setuptools import (
        setup as _setup,
        find_packages
    )
    from pathlib import Path

    dir_path = Path(__file__).parent
    description = __doc__ or ''
    long_description = (dir_path / 'README.md').read_text() or description

    author = maintainer = 'Jacob Chesslo'
    author_email = maintainer_email = 'jacobchesslo@gmail.com'
    url = download_url = 'https://www.github.com/jacobchesslo/behaviorpy'

    return _setup(

        # Metadata
        name='behaviorpy',
        version='0.1.0',
        description=description,
        long_description=long_description, long_description_content_type='text/markdown',
        # https://pypi.org/classifiers/
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Education',
            'Intended Audience :: Science/Research',
            'Natural Language :: English',
            'Operating System :: MacOS',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Topic :: Scientific/Engineering',
        ],

        # Credits
        author=author, author_email=author_email,
        maintainer=maintainer, maintainer_email=maintainer_email,

        # Links
        url=url, download_url=download_url,

        # Packages
        packages=find_packages(
            exclude=[
                'tests', '*.tests', '*.tests.*', 'tests.*',
                'examples', '*.examples', '*.examples.*', 'examples.*',
            ]
        ),

        # Requirements
        python_requires='>3.6.5',
        install_requires=(dir_path / 'requirements.txt').read_text().splitlines(keepends=False) or [
            'numpy',
            'matplotlib'
        ],
        extra_requires={

        },
        setup_requires=[
            'setuptools>=52.0.0',
        ],
    )


if __name__ == '__main__':
    setup()
