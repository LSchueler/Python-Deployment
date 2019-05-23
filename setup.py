# -*- coding: utf-8 -*-
"""Python Deployment"""
import sys, os, codecs, re, tempfile, glob, subprocess, shutil

from distutils.errors import CompileError, LinkError
from distutils.ccompiler import new_compiler
from distutils.sysconfig import customize_compiler

from setuptools import setup, find_packages, Distribution, Extension
from Cython.Build import cythonize
import numpy


HERE = os.path.abspath(os.path.dirname(__file__))


# version finder ##############################################################


def read(*file_paths):
    """read file data"""
    with codecs.open(os.path.join(HERE, *file_paths), "r") as file_in:
        return file_in.read()


def find_version(*file_paths):
    """find version without importing module.
    This is useful in case the project is using Cython.
    """
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# cython extensions ###########################################################

FLAGS = []

EXT_MODULES = []

EXTRA_COMPILE_ARGS = FLAGS
EXTRA_LINK_ARGS = FLAGS

MATMUL_EXT = Extension(
    'deployment.matmul',
    [os.path.join('deployment', 'matmul.pyx')],
    include_dirs=[numpy.get_include()],
    extra_compile_args=EXTRA_COMPILE_ARGS,
    extra_link_args=EXTRA_LINK_ARGS,
)

EXT_MODULES += cythonize(
    [MATMUL_EXT],
    # annotate=True
)

# By setting this compiler directive, cython will embed signature information
# in docstrings. Sphinx then knows how to extract and use those signatures.
# python setup.py build_ext --inplace --> then sphinx build
for ext_m in EXT_MODULES:
    ext_m.cython_directives = {"embedsignature": True}
# setup #######################################################################


# version import not possible due to cython
# see: https://packaging.python.org/guides/single-sourcing-package-version/
VERSION = find_version("deployment", "_version.py")
DOCLINES = __doc__.split("\n")
README = read("README.md")

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Natural Language :: English",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Utilities",
]

setup(
    name="python-deployment",
    version=VERSION,
    maintainer="Lennart Schueler",
    maintainer_email="mostem@posteo.org",
    description=DOCLINES[0],
    long_description=README,
    long_description_content_type="text/markdown",
    author="Lennart Schueler",
    author_email="mostem@posteo.org",
    url="https://github.com/LSchueler/Python-Deployment",
    license="GPL -  see LICENSE",
    classifiers=CLASSIFIERS,
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    include_package_data=True,
    setup_requires=[
        "numpy>=1.14.5",  # numpy imported in setup.py
        "cython>=0.28.3",
        "setuptools>=41.0.1",
    ],
    install_requires=[
        "numpy>=1.14.5",
    ],
    packages=find_packages(exclude=["tests*", "docs*"]),
    ext_modules=EXT_MODULES,
    include_dirs=[numpy.get_include()],
)
