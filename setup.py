#!/usr/bin/env python
"""wavefunction: a python package for computing wavefunctions and energy
spectrum for arbitrary one and two-dimensional quantum systems.
"""

DOCLINES = __doc__.split('\n')

CLASSIFIERS = """\
Programming Language :: Python
Topic :: Engineering
Operating System :: POSIX
Operating System :: Unix
"""

import os
import sys
import shutil
import re
import subprocess
import warnings
from distutils.core import setup, Extension
import numpy as np


MAJOR = 1
MINOR = 0
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
REVISION = 0 + int(os.popen("git rev-list --all | wc -l").read())


def write_version_py(filename='wavefunction/version.py'):
    if os.path.exists(filename):
        os.remove(filename)
    cnt = """\
# THIS FILE IS AUTOMATICALLY GENERATED BY WAVEFUNCTION SETUP.PY
version = '%(version)s'
revision = %(revision)s
release = %(isrelease)s
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': VERSION,
                       'revision': REVISION,
                       'isrelease': str(ISRELEASED)})
    finally:
        a.close()

write_version_py()

setup(
    name="wavefunction",
    version=VERSION,
    packages=['wavefunction'],
    include_dirs=[np.get_include()],
    author="Robert Johansson",
    author_email="jrjohansson@gmail.com",
    license="LGPL",
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    keywords="compute wavefunctions and energy spectra",
    url="http://github.com/jrjohansson",
    platforms=["Linux", "Unix"],
)
