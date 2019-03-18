from encpoly import encode


def test_encode():
    coords = ((38.5, -120.2), (40.7, -120.95), (43.252, -126.453))
    assert encode(coords) == "_p~iF~ps|U_ulLnnqC_mqNvxq`@"
