Pip2Arch
=======

Pip2Arch converts entries in the pypi database to Arch Linux PKGBUILDS, allowing the user to harness both the power of pacman, the arch linux package manager, and the sheer amount of python modules in pypi.

Usage
-----

`pip2arch.py django-sentry` will create a PKGBUILD for the django-sentry python package. Run `pip2arch --help` for more information on the various arguments possible.

A quick runthrough:

* `-d` -- manually add a dependency
* `-m` -- manually add a maketime dependency
* `-o` -- specify the output file
* `-n` -- specify the name of the outputted package
* `-v` -- the version of the PiPy package to use
* `-s` -- search for package instead of building a PKGBUILD

Problems
--------

Does not deal with dependencies, due to unreliable returns from the pypi xmlrpc api. If pypi were to fix this, which they can, then adding dependencies would not be at all hard. 


Get Involved
============

Cheesy section, but still. I prefer patches via the github merge request system, and failing that, using `git-email` (which is a pain to setup, but an excelent tool).

Fork the repo, pull the code, hack about, and send it too me.

TODO
----

* Patch the pypi website to return dependencies?
* Add some nice arguments
* ???
* Profit

PyPi xmlrpc Doc
---------------

`xmlrpc` documentation can be found here: [PyPiXmlRpc Doc](http://wiki.python.org/moin/PyPiXmlRpc)
