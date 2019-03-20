"""
Encode and decode coordinates using Google's Encoded Polyline Algorithm.

The `Encoded Polyline Algorithm`_ is a lossy compression algorithm that
allows you to store a series of geographical coordinates as a single
string. It was developed by Google.

The encoding process converts a longitude or latitude coordinate from a
decimal value to a binary value, and then converts that into a series of
ASCII characters. To further compress the data, values stored for
longitude and latitude are offset from the previous longitude or
latitude values. The algorithm is lossy because it uses a default
maximum precision of five decimal places for longitude and latitude.

.. _Encoded Polyline Algorithm: https://developers.google.com/maps/documentation/utilities/polylinealgorithm
"""
from itertools import chain
from math import floor, ceil
from operator import sub


#: When encoding values of longitude and latitude, use a default precision of
#: five decimal places. This gives, very roughly, accuracy of one metre.
DEFAULT_PRECISION = 1e5


def polyline_round(number):
    """
    Return the given number rounded to nearest integer.

    >>> polyline_round(0.5)
    1
    >>> polyline_round(-0.5)
    -1

    Note:
        The rounding behaviour is "always round up 0.5". This is not
        generally considered the standard way of rounding numbers now
        (Python 3 does it differently, for example). But it is what
        Python 2 does by default and it is, not coincidentally, what the
        Encoded Polyline Algorithm requires.

    Args:
        number (float): value to round to nearest integer

    Returns:
        int
    """
    if number > 0:
        return floor(number + 0.5)
    else:
        return ceil(number - 0.5)


def encode_coord(coord, precision):
    """
    Encode a given longitude or latitude value as an encoded polyline.

    The encodes an individual value from a lat/lon pair into an ASCII
    value that can be used in an encoded polyline.

    Tip:
        You probably want to use :func:`encpoly.encode` instead, as that
        function will encode a complete line (that is, a set of lat/lon
        pairs).

    >>> encode_coord(-179.9832104, 1e5)
    '`~oia@'

    Args:
        coord (float): a single latitude or longitude coordinate
        precision (float): maximum decimal precision used to store the
            coordinate value

    Returns:
        str: the coordinate value as an encoded polyline
    """
    coord = polyline_round(coord * precision) << 1  # Steps 1–4.
    if coord < 0:
        coord = ~coord  # Step 5.
    encoded_coord = ""
    # The while loop handles steps 6–11 of the algorithmic encoding.
    while coord >= 0x20:
        encoded_coord += chr((0x20 | (coord & 0x1F)) + 63)  # Steps 8–10.
        coord >>= 5
    # Add the final (leftover) chunk. Step 8 not required because we
    # know there's no following chunk.
    encoded_coord += chr(coord + 63)  # Steps 9–10.
    return encoded_coord


def encode(locations, precision=None):
    """
    Encode the given coordinates as an encoded polyline.

    >>> coords = ((38.5, -120.2), (40.7, -120.95), (43.252, -126.453))
    >>> encode(coords)
    '_p~iF~ps|U_ulLnnqC_mqNvxq`@'

    To produce an encoded polyline, follow these steps for each
    individual longitude and latitude value.

    1.  Take a signed longitude or latitude decimal value and multiply
        it by 1e5 (or other decimal precision if specified)
    2.  Round the result using Python 2's default rounding behaviour
    3.  Convert the decimal value to binary (a negative value must be
        calculated using its two's complement)
    4.  Shift the binary value left by one bit
    5.  If the original decimal value is negative, invert the encoding
    6.  Break the binary value out into 5-bit chunks from right to left
    7.  Place the 5-bit chunks into reverse order
    8.  OR each value with 0x20 if another bit chunk follows
    9.  Convert each value to decimal
    10. Add 63 to each value (this is to avoid, e.g., unprintable ASCII
        characters)
    11. Convert each value to its ASCII equivalent

    Note:
        After the first latitude/longitude pair, the steps should be
        followed using offsets from the previous point.

        If coordinates are provided with a greater decimal precision
        than is used during step 1, the resulting output will be lossy.

    Args:
        locations (iterable): ordered latitude and longitude pairs (in
            y, x order) as a tuple, list, or other iterable
        precision (int): maximum decimal precision to use for longitude
            and latitude coordinates (defaults to 5)

    Returns:
        str: an encoded polyline
    """
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
    """
    Yield alternating latitude and longitude values from a polyline.

    Each coordinate is an offset from the last of its type, and has yet
    to be converted from its stored integer value to a floating point
    coordinate (see steps 1 and 2 of the encoding algorithm).

    Tip:
        You probably want to use :func:`encpoly.decode` instead, as that
        function returns lat/lon pairs with offset and precision handled
        correctly.

    >>> tuple(decode_coords("_p~iF~ps|U_ulLnnqC_mqNvxq`@"))
    (3850000, -12020000, 220000, -75000, 255200, -550300)

    Args:
        polyline (str): encoded polyline to decode

    Yields:
        iterable of alternating lat/lon coordinates
    """
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
    """
    Yield the given encoded polyline as an ordered series of points.

    This essentially reverses the algorithm's steps as outlined in the
    :func:`encode` documentation.

    >>> for coord in decode("_p~iF~ps|U_ulLnnqC_mqNvxq`@"):
    ...     print(coord)
    ...
    [38.5, -120.2]
    [40.7, -120.95]
    [43.252, -126.453]

    Args:
        polyline (str): encoded polyline to decode
        precision (int): maximum decimal precision used when the
            polyline was originally encoded (defaults to 5)

    Yields:
        iterable of lists of lat/lon coordinate pairs
    """
    if precision is None:
        precision = DEFAULT_PRECISION
    else:
        precision = 10 ** precision
    prev_location = (0, 0)
    i = decode_coords(polyline)  # Actual decoding handled by `decode_coords`.
    for coord in i:
        # Except for the first pair, decoded lat/lon coordinates are stored as
        # offsets from the previous coordinate. Here they're converted to
        # absolute values.
        location = [coord + prev_location[0], next(i) + prev_location[1]]
        # Final step is to convert from integers to floats with specified
        # precision. E.g. for precision=5, value 12345000 equals coord 123.45.
        yield [p / precision for p in location]
        prev_location = location
