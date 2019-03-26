Introduction
============

The encpoly package is a Python 3 library for encoding/decoding geographic coordinates using `Google's Encoded Polyline Algorithm`_. The package is `developed on GitHub`_ and contributions are welcome.

Table of contents
-----------------

.. toctree::
   :maxdepth: 1

   installation
   api

Quick start
-----------

>>> from encpoly import encode, decode
>>> coords = ((38.5, -120.2), (40.7, -120.95), (43.252, -126.453))
>>> encode(coords)
'_p~iF~ps|U_ulLnnqC_mqNvxq`@'
>>> tuple(decode("_p~iF~ps|U_ulLnnqC_mqNvxq`@"))
([38.5, -120.2], [40.7, -120.95], [43.252, -126.453])

Elsewhere
---------

* `Repository on GitHub`_
* `Package on PyPI`_
* `Bug reports and issues`_
* Changelog_
* Licence_
* Contributors_


.. _Google's Encoded Polyline Algorithm: https://developers.google.com/maps/documentation/utilities/polylinealgorithm
.. _developed on GitHub: https://github.com/JaGallup/encpoly
.. _Repository on GitHub: https://github.com/JaGallup/encpoly
.. _Package on PyPI: https://pypi.org/project/encpoly/
.. _Bug reports and issues: https://github.com/JaGallup/encpoly/issues
.. _Changelog: https://github.com/JaGallup/encpoly/blob/master/CHANGELOG.md
.. _Licence: https://github.com/JaGallup/encpoly/blob/master/LICENCE
.. _Contributors: https://github.com/JaGallup/encpoly/graphs/contributors
