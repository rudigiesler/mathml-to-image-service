import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
import requests
from config import mathoid_url


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
    try:
        ET.fromstring(mathml)
    except ParseError as e:
        raise SVGEncodeError("Invalid MathML %s" % e)
    r = requests.post(mathoid_url, data={'q': mathml, 'type': 'mml'})
    if r.text is None or 'Error parsing MathML: ' in r.text:
        raise SVGEncodeError("Conversion error")
    return r.text
