from encpoly import encode
from encpoly.codec import polyline_round


def test_polyline_round():
    assert polyline_round(0) == 0

    assert polyline_round(0.5) == 1
    assert polyline_round(1) == 1
    assert polyline_round(1.5) == 2
    assert polyline_round(2.5) == 3
    assert polyline_round(3.5) == 4

    assert polyline_round(-0.5) == -1
    assert polyline_round(-1) == -1
    assert polyline_round(-1.5) == -2
    assert polyline_round(-2.5) == -3
    assert polyline_round(-3.5) == -4


def test_encode():
    coords = ((38.5, -120.2), (40.7, -120.95), (43.252, -126.453))
    assert encode(coords) == "_p~iF~ps|U_ulLnnqC_mqNvxq`@"


def test_precision():
    coords = (
        (123.46, 234.57),
        (123.0, -234.0),
        (-123.5, 234.5),
        (-123.5, -234.5),
    )
    assert encode(coords, precision=2) == "sbWayl@zApozArco@cozA?frzA"
