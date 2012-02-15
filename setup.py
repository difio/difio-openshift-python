#!/usr/bin/python

import _version
from distutils.core import setup

with open('README.txt') as file:
    long_description = file.read()

setup(
    name=_version.name,
    version=_version.version,
    description='monupco.com client for OpenShift Express / wsgi-3.2 applications',
    author='Alexander Todorov',
    author_email='atodorov@nospam.otb.bg',
    url = 'http://monupco.com',
    scripts=['monupco-openshift-express-python'],
    keywords = ['openshift', 'monupco', 'updates', 'cloud'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: System",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
        ],
    long_description = long_description,
     )
