==============================
Contribution
==============================

.. _gettingstarted

Getting started
---------------

What open source project doesn't like getting contributions? Don't hesitate to
send us feature requests, bug reports, bug fixes, or pull requests.

.. contents:: Contribution links
    :depth: 1

.. _submitfeedback:

Feature Requests
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
#. Clone the repository from your account into your local file system::

    git clone git@github.com:<username>/pyzu.git
#. Setup your upstream origin, and make sure your forked code has the latest
   code::

    git remote add upstream https://github.com/chason/pyzu.git
    git fetch upstream
    git checkout master
    git merge upstream/master

#. Create new branch::

    git checkout -b my_awesome_feature

#. Write new code following the :ref:`codestyle`
#. Run tests::

    pytest

#. Commit your code, mentioning the issue number in the description::

    git add *
    git commit -m "Fixing issue #1"

#. Push the code to your origin::

    git push origin

#. Point your web browser to the Github page for the project and click on the
   `New pull request` button. `GitHub documentation
   <https://help.github.com/articles/creating-a-pull-request-from-a-fork/>`_
#. Pat yourself on the back for a job well done!

.. _codestyle:

Code Style Guidelines
-----------------------

To create a consistent code style across the codebase its important to follow
a few rules.

All new code should meet the following guidelines:

* PEP-8 for the most part, except for line length (set at 88).
* Use `black <https://github.com/ambv/black>`_ for formatting.
* Use type hinting everywhere.
* Public methods should have a docstring that describes their use, parameters,
  and output.
* 100% test code coverage

