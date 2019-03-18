Introduction
============

The encpoly package is a Python 3 library for encoding/decoding geographic coordinates using `Google's Encoded Polyline Algorithm`_. The package is `developed on GitHub`_ and contributions are welcome.

Usage
-----

>>> from encpoly import encode, decode
>>> coords = ((38.5, -120.2), (40.7, -120.95), (43.252, -126.453))
>>> encode(coords)
'_p~iF~ps|U_ulLnnqC_mqNvxq`@'
>>> tuple(decode("_p~iF~ps|U_ulLnnqC_mqNvxq`@"))
([38.5, -120.2], [40.7, -120.95], [43.252, -126.453])


.. _Google's Encoded Polyline Algorithm: https://developers.google.com/maps/documentation/utilities/polylinealgorithm
.. _developed on GitHub: https://github.com/JaGallup/encpoly
