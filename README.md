Pip2Arch
=======

Pip2Arch converts entries in the pypi database to Arch Linux PKGBUILDS, allowing the user to harness both the power of pacman, the arch linux package manager, and the sheer amount of python modules in pypi.

Usage
-----

# pip2arch django-sentry

will create a PKGBUILD in the pip2arch dir for the django-sentry python package.

Problems
--------

Does not deal with dependencies, due to unreliable returns from the pypi xmlrpc api. If pypi were to fix this, which they can, then adding dependencies would not be at all hard. 

TODO
----

* Patch the pypi website to return dependencies?
* Add some nice arguments
* ???
* Profit

PyPi xmlrpc Doc
---------------

xmlrpc documentation can be found here: http://wiki.python.org/moin/PyPiXmlRpc
