==============================
Contribution getting started
==============================

What open source project doesn't like getting contributions? Don't hesitate to
send us feature requests, bug reports, bug fixes, or pull requests.

.. contents:: Contribution links
    :depth: 1

.. _submitfeedback:

Feature requests
-------------------

We are happy to consider new features, but be aware that we feel libraries are
best when small and focused so not everything will be considered. `Submit them
as issues <https://github.com/chason/pyzu/issues>`_ and:

* Explain in detail why this feature is necessary/useful
* Step through exactly how it should work. The more detail the better.

.. _reportbugs

Report bugs
---------------

Reporting bugs is one of the most valuable things you can do, when done
properly.

Report all bugs for pyzu in the `issue tracker
<https://github.com/chason/pyzu/issues>`_.

Please include the following in any bug report:

* Your operating system name and version.
* The version of Python you are using, as well as any other useful information
  about your environment (library version, etc).
* Any relevant tracebacks.
* Detailed steps to reproduce the bug.

If you can write a test that currently fails but should pass, that is an
extremely valuable contribution, even if you cannot fix the bug itself.

.. _fixbugs:

Fixing bugs
-------------

Look through the `GitHub issues for bugs
<https://github.com/chason/pyzu/labels/type:%20bug>`_.

A good bug fix will include:

* Tests to ensure the bug is fixed and stays fixed.
* A link to the appropriate issue in the pull request.

.. _`pull requests`:

Preparing Pull Requests
------------------------

#. Fork the repository
#. Follow **PEP-8** for naming and `black <https://github.com/ambv/black>`_ for
   formatting.
#. Tests are run using `py.test`::

    pytest --cov-report term-missing --cov=pyzu --mypy --flake8

.. _codestyle:

Code Style Guidelines
-----------------------

To create a consistent code style across the codebase its important to follow
a few rules.

All new code should meet the following guidelines:

* PEP-8 for the most part, except for line length (set at 88).
* Use `black <https://github.com/ambv/black>`_ for formatting.
* Use type hinting everywhere.
* Public methods should have a docstring that describes their use, paramters,
  and output.
* 100% test code coverage

