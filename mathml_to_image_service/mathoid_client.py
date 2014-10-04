from config import mathoid_url
import requests


class SVGEncodeError(Exception):
    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return "SVGEncodeError: " + '\n'.join(self.errors)


def get_svg(mathml):
    """
    Makes a request to the mathoid API to convert the given MathML to SVG.

    :param str mathml: The MathML to be converted.
    """
    r = requests.post(mathoid_url, data={'q': mathml})
    data = r.json()
    if data.get('success') is False:
        raise SVGEncodeError(data.get('errors'))
    return data.get('svg')
