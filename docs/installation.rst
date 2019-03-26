Installation and usage
======================

.. image:: https://img.shields.io/pypi/v/encpoly.svg
   :target: https://pypi.org/project/encpoly/
   :height: 20
   :width: 78
   :align: right

The `latest encpoly release is available on PyPI`_, and you can install it using Pip_::

    pip install encpoly

.. tip:: When installing Python dependencies, it's a good idea to use a `virtual environment`_.

If you prefer, you can also install encpoly using a higher-level dependency-management tool like Poetry_::

    poetry add encpoly

Or Pipenv_::

    pipenv install encpoly

System requirements
-------------------

The encpoly package requires Python 3.4+. It runs well under PyPy_. It has no dependencies of its own. It's multi-platform and works on Linux, MacOS, and Windows.

Usage
-----

After you've installed the package you can import the :func:`~encpoly.encode` and :func:`~encpoly.decode` functions from the :mod:`encpoly` package:

>>> from encpoly import encode, decode

To encode a series of coordinates, pass them to the :func:`~encpoly.encode` function:

>>> coords = ((38.5, -120.2), (40.7, -120.95), (43.252, -126.453))
>>> encode(coords)
'_p~iF~ps|U_ulLnnqC_mqNvxq`@'

To decode a polyline, pass it to the :func:`~encpoly.decode` function:

>>> for (lat, lon) in decode("_p~iF~ps|U_ulLnnqC_mqNvxq`@"):
...     print(lat, lon)
...
38.5 -120.2
40.7 -120.95
43.252 -126.453

.. tip:: The :func:`~encpoly.decode` function returns a generator_. If you want to get a list or tuple of coordinates rather than a generator, wrap the function in :class:`list` or :class:`tuple`:

  >>> tuple(decode("_p~iF~ps|U_ulLnnqC_mqNvxq`@"))
  ([38.5, -120.2], [40.7, -120.95], [43.252, -126.453])

You'll probably not need anything other than those two functions, but the full contents of the package are documented in the :doc:`api`.

Advanced usage
--------------

By default the `Encoded Polyline Algorithm`_ is lossy. When coordinates are encoded they are truncated to five decimal places. For example, the latitude and longitude coordinates 64.12345678, -21.987654321 would be encoded as 64.12345, -21.98765:

>>> list(decode(encode(((64.12345678, -21.987654321),))))
[[64.12346, -21.98765]]

You can, however, choose the precision at which coordinates are encoded using the ``precision`` argument:

    >>> coords = ((64.12345678, -21.987654321),)
    >>> encode(coords)
    'sbkfKxmeeC'
    >>> encode(coords, precision=8)
    '{soqe}Jnv~x`bC'
    >>> list(decode("{soqe}Jnv~x`bC", precision=8))
    [[64.12345678, -21.98765432]]

.. note:: You must use the same value for ``precision`` when encoding and decoding. You can only set the precision for polylines as a whole, not individual coordinates within a polyline.

Package development
-------------------

Encpoly is an open-source project and all contributions are welcome. Encpoly is `developed on GitHub`_ and the latest source code is always available from there. To get a copy of the code you can clone the public repository::

    $ git clone https://github.com/JaGallup/encpoly.git

To install the package in `"editable mode"`_ you will need Poetry_, a tool for dependency management and packaging in Python. Once you have both Poetry and a copy of the source you can install encpoly and its development dependencies into a virtual environment::

    $ cd encpoly
    $ poetry install

Test suite
~~~~~~~~~~

Encpoly uses Pytest_ and Tox_ for testing. To run the tests locally, use::

    tox -e py37

The example above runs tests against Python 3.7. You can also use other versions like ``py36`` and ``pypy3``.

The test suite is run automatically when the master branch is pushed to GitHub. The tests are run using `Travis CI`_ (Linux) and Appveyor_ (Windows) for Python 3.4+ and PyPy 3.5. Code coverage is tracked using Codecov_.

.. image:: https://travis-ci.org/JaGallup/encpoly.svg?branch=master
   :alt: Build status on Travis CI
   :target: https://travis-ci.org/JaGallup/encpoly
   :height: 20
   :width: 90

.. image:: https://ci.appveyor.com/api/projects/status/6lu5j29y6e22dken?svg=true
   :alt: Build status on Appveyor
   :target: https://ci.appveyor.com/project/flother/encpoly
   :height: 20
   :width: 106

.. image:: https://codecov.io/gh/JaGallup/encpoly/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/JaGallup/encpoly
   :height: 20
   :width: 122


.. _latest encpoly release is available on PyPI: https://pypi.org/project/encpoly/
.. _Pip: https://pip.pypa.io/
.. _virtual environment: https://virtualenv.pypa.io/
.. _Poetry: https://poetry.eustace.io/
.. _Pipenv: https://pipenv.readthedocs.io/
.. _PyPy: https://www.pypy.org/
.. _generator: https://realpython.com/introduction-to-python-generators/
.. _Encoded Polyline Algorithm: https://developers.google.com/maps/documentation/utilities/polylinealgorithm
.. _developed on GitHub: https://github.com/JaGallup/encpoly
.. _"editable mode": https://pip.pypa.io/en/latest/reference/pip_install/#editable-installs
.. _Pytest: https://docs.pytest.org/
.. _Tox: https://tox.readthedocs.io/
.. _Travis CI: https://travis-ci.org/JaGallup/encpoly
.. _Appveyor: https://ci.appveyor.com/project/flother/encpoly
.. _Codecov: https://codecov.io/gh/JaGallup/encpoly
