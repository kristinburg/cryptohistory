Crypto History
==============

Testing
-------

::

    $ pip install -r requirements-testing.txt
    $ pytest


Coverage
--------

Use coverage for an overview on how much the tests cover the project.
Warning: 100% coverage doesn't mean 100% branch-coverage. Even 100% branch-coverage
is no guaruantee that everything is tested (this is not possible).
See coverage as a guideline to make tests.

::

    $ coverage run --source . -m pytest && coverage html
