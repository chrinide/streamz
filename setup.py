#!/usr/bin/env python

from os.path import exists
from setuptools import setup


setup(name='streamz',
      version='0.1.0',
      description='Streams',
      url='http://github.com/mrocklin/streamz/',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      license='BSD',
      keywords='streams',
      packages=['streamz'],
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      install_requires=list(open('requirements.txt').read().strip().split('\n')),
      zip_safe=False)
