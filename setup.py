#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    find_packages,
    setup,
)

setup(
    name='augurV2Migration',
    version='1.0.0',
    description="""Augur V2 Migration""",
    long_description_content_type='text/markdown',
    long_description_markdown_filename='README.md',
    author='Alex Chapman',
    author_email='achapman@augur.net',
    url='https://github.com/augurproject/V2Migration',
    include_package_data=True,
    install_requires=[
        "attrdict==2.0.1",
        "web3==5.9.0",
        "hidapi>=0.7.99",
    ],
    setup_requires=['setuptools-markdown'],
    python_requires='>=3.6,<4',
    py_modules=['web3'],
    entry_points = {
        'console_scripts': ['migrate=migrate.command_line:main'],
    },
    license="MIT",
    zip_safe=False,
    keywords='augur',
    packages=find_packages(),
    package_data={"augurV2Migration": ["py.typed"]},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)