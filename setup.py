import io
import os
import re

from distutils.core import setup


def read(path, encoding='utf-8'):
    path = os.path.join(os.path.dirname(__file__), path)
    with io.open(path, encoding=encoding) as fp:
        return fp.read()


def version(path):
    """Obtain the packge version from a python file e.g. pkg/__init__.py

    See <https://packaging.python.org/en/latest/single_source_version.html>.
    """
    version_file = read(path)
    version_match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


DESCRIPTION = "Flexible and scikit-learn compatible Mapper implementation"
LONG_DESCRIPTION = """
cartographer: Flexible and scikit-learn compatible Mapper implementation
======================================================

This package implements a scikit-learn API compatible implementation of
the Mapper algorithm.

For more information, visit http://github.com/pablodecm/cartographer
"""
NAME = "cartographer"
AUTHOR = "Pablo de Castro"
AUTHOR_EMAIL = "pablodecm@gmail.com"
MAINTAINER = "Pablo de Castro"
MAINTAINER_EMAIL = "pablodecm@gmail.com"
URL = 'http://github.com/pablodecm/cartographer'
DOWNLOAD_URL = 'http://github.com/pablodecm/cartographer'
LICENSE = 'MIT'

VERSION = version('cartographer/__init__.py')

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['cartographer',
                'cartographer.tests',
                ],
      package_data={'cartographer': ['graph_template.html']},
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5'],
      )
