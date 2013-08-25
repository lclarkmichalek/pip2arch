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
* `-v` -- the version of the PyPi package to use
* `-v` -- the python version to build and install the package with {python,python2} (default: python)
* `-s` -- search for package instead of building a PKGBUILD
* `-i` -- make commands interactive
* `-b` -- add custom arguments to the setup.py call in the PKGBUILD
* `--logging-level` -- specify the logging level for pip2arch to run at {warning, info, debug} (default: warning)

Problems
--------

Dependencies are only as good as PyPi's are, which is not very brilliant. Dependencies do not allways link in nicely with other PyPi generated packages (though that may be fixed in future versions).

Get Involved
============

Cheesy section, but still. I prefer patches via the github merge request system, and failing that, using `git-email` (which is a pain to setup, but an excelent tool).

Fork the repo, pull the code, hack about, and send it too me.

PyPi xmlrpc Doc
---------------

`xmlrpc` documentation can be found here: [PyPiXmlRpc Doc](http://wiki.python.org/moin/PyPiXmlRpc)
