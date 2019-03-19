from itertools import chain
from math import floor, ceil
from operator import sub


DEFAULT_PRECISION = 1e5


def polyline_round(number):
    if number > 0:
        return floor(number + 0.5)
    else:
        return ceil(number - 0.5)


def encode_coord(coord, precision):
    coord = polyline_round(coord * precision) << 1
    if coord < 0:
        coord = ~coord
    encoded_coord = ""
    while coord >= 0x20:
        encoded_coord += chr((0x20 | (coord & 0x1F)) + 63)
        coord >>= 5
    encoded_coord += chr(coord + 63)
    return encoded_coord


def encode(locations, precision=None):
    if precision is None:
        precision = DEFAULT_PRECISION
    else:
        precision = 10 ** precision
    encoded_coords = []
    prev_location = (0, 0)
    for location in locations:
        encoded_coords.append(
            encode_coord(p, precision)
            for p in map(sub, location, prev_location)
        )
        prev_location = location
    return "".join(chain(*encoded_coords))


def decode_coords(polyline):
    coord = 0
    shift = 0
    for char in map(ord, polyline):
        char -= 63
        coord |= (char & 0x1F) << shift
        shift += 5
        if char < 0x20:
            if coord & 1:
                yield ~coord >> 1
            else:
                yield coord >> 1
            coord = 0
            shift = 0


def decode(polyline, precision=None):
    if precision is None:
        precision = DEFAULT_PRECISION
    else:
        precision = 10 ** precision
    prev_location = (0, 0)
    i = decode_coords(polyline)
    for coord in i:
        location = [coord + prev_location[0], next(i) + prev_location[1]]
        yield [p / precision for p in location]
        prev_location = location
