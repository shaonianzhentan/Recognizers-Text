#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


NAME = 'ms-recognizers-text-suite'
VERSION = '1.0.1'
REQUIRES = ['ms-recognizers-text', 'ms-recognizers-text-number', 'ms-recognizers-text-number-with-unit',
            'ms-recognizers-text-date-time', 'ms-recognizers-text-sequence', 'ms-recognizers-text-choice']

setup(
    name=NAME,
    version=VERSION,
    url='https://github.com/Microsoft/Recognizers-Text',
    author='Microsoft',
    description='recognizers-text-suite README',
    keywords=['nlp', 'nlp-entity-extraction',
              'entity-extraction', 'parser-library'],
    long_description=read('README.rst'),
    license='MIT',
    packages=find_packages(),
    install_requires=REQUIRES,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)
