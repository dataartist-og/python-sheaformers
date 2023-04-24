========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-sheaformers/badge/?style=flat
    :target: https://python-sheaformers.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/dataartist-og/python-sheaformers/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/dataartist-og/python-sheaformers/actions

.. |version| image:: https://img.shields.io/pypi/v/sheaformers.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/sheaformers

.. |wheel| image:: https://img.shields.io/pypi/wheel/sheaformers.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/sheaformers

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sheaformers.svg
    :alt: Supported versions
    :target: https://pypi.org/project/sheaformers

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sheaformers.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/sheaformers

.. |commits-since| image:: https://img.shields.io/github/commits-since/dataartist-og/python-sheaformers/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/dataartist-og/python-sheaformers/compare/v0.0.0...main



.. end-badges

Construct sheaves and reason over them.

Installation
============

::

    pip install sheaformers

You can also install the in-development version with::

    pip install https://github.com/dataartist-og/python-sheaformers/archive/main.zip


Documentation
=============


https://python-sheaformers.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
