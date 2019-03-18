The `encpoly` package is a Python 3 library for fast, Pythonic manipulation of [encoded polylines][].

[![Build status][tci]][tcl]
[![Code coverage report][cci]][ccl]

```python
>>> from encpoly import encode, decode
>>> coords = ((38.5, -120.2), (40.7, -120.95), (43.252, -126.453))
>>> encode(coords)
'_p~iF~ps|U_ulLnnqC_mqNvxq`@'
>>> tuple(decode("_p~iF~ps|U_ulLnnqC_mqNvxq`@"))
([38.5, -120.2], [40.7, -120.95], [43.252, -126.453])
```

  [encoded polylines]: https://developers.google.com/maps/documentation/utilities/polylinealgorithm
  [tci]: https://travis-ci.org/JaGallup/encpoly.svg?branch=master
  [tcl]: https://travis-ci.org/JaGallup/encpoly
  [cci]: https://codecov.io/gh/JaGallup/encpoly/branch/master/graph/badge.svg
  [ccl]: https://codecov.io/gh/JaGallup/encpoly
