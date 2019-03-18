from encpoly import decode


def test_decode():
    coords = ([38.5, -120.2], [40.7, -120.95], [43.252, -126.453])
    encoded_polyline = "_p~iF~ps|U_ulLnnqC_mqNvxq`@"
    assert tuple(decode(encoded_polyline)) == coords
