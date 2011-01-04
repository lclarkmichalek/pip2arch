#!/usr/bin/env python
from distutils.core import setup
setup(  name="pip2arch",
        version="0.1",
        description="Convert pypi packages to Arch Linux PKGBUILDs",
        author="Laurie Clark-Michalek",
        author_email="BluePeppers@archlinux.us",
        scripts=["pip2arch.py"],
        download_url=["http://github.com/bluepeppers/pip2arch/tarball/master"],
        url=["http://github.com/bluepeppers/pip2arch"],
        classifiers=[
            "Environment :: Console",
            "Intended Audience :: End Users/Desktop",
            "Natural Language :: English",
            "Operating System :: OS Independent"
            ]
        )
