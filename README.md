The `encpoly` package is a Python 3 library for fast, Pythonic manipulation of [encoded polylines][].

[![Build status][tci]][tcl]
[![Code coverage report][cci]][ccl]
[![Package on PyPI][ppi]][ppl]

```python
>>> from encpoly import encode, decode
>>> coords = ((38.5, -120.2), (40.7, -120.95), (43.252, -126.453))
>>> encode(coords)
'_p~iF~ps|U_ulLnnqC_mqNvxq`@'
>>> tuple(decode("_p~iF~ps|U_ulLnnqC_mqNvxq`@"))
([38.5, -120.2], [40.7, -120.95], [43.252, -126.453])
```

You can use Pip to install the [latest release][] from PyPi:

    pip install encpoly

  [encoded polylines]: https://developers.google.com/maps/documentation/utilities/polylinealgorithm
  [tci]: https://travis-ci.org/JaGallup/encpoly.svg?branch=master
  [tcl]: https://travis-ci.org/JaGallup/encpoly
  [cci]: https://img.shields.io/codecov/c/github/JaGallup/encpoly.svg
  [ccl]: https://codecov.io/gh/JaGallup/encpoly
  [ppi]: https://img.shields.io/pypi/v/encpoly.svg
  [ppl]: https://pypi.org/project/encpoly/
  [latest release]: https://github.com/JaGallup/encpoly/releases
