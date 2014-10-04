from config import mathoid_url
import requests


class SVGEncodeError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return "SVGEncodeError: %s" % self.error


def get_svg(mathml):
    """
    Makes a request to the mathoid API to convert the given MathML to SVG.

    :param str mathml: The MathML to be converted.
    """
    r = requests.post(mathoid_url, data={'q': mathml, 'type': 'mml'})
    if r.text is None:
        raise SVGEncodeError("Conversion error")
    return r.text
