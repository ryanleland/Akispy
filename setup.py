#!/usr/bin/env python

from setuptools import setup

import akispy

setup(
    name="akispy",
    version=akispy.__version__,
    description=akispy.__doc__,
    url="https://github.com/ryanleland/Akispy",
    author=akispy.__author__,
    author_email='me@ryanleland.com',
    packages = [
        'akispy'
    ],
    
    package_data={'': ['LICENSE']},
    include_package_data=True,
    license=open("LICENSE").read(),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    )
)