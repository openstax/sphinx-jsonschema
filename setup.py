#!/usr/bin/env python

from distutils.core import setup

setup(name='sphinx-jsonschema',
      version='0.0.1',
      description='JSON schema directive for sphinx',
      author='navilan',
      author_email='navilan@folds.in',
      py_modules=['sphinx_jsonschema'],
      install_requires=('sphinx', 'sphinxcontrib-httpdomain'))
