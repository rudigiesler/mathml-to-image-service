import os
import re
import unittest

from mathml_to_image_service.svg_to_image import to_image, ImageConvertError
from mathml_to_image_service.config import STATIC_DIR


class SVGToImageTestCase(unittest.TestCase):
    def test_create_image(self):
        with open('mathml_to_image_service/tests/mathoid_test_data.svg') as f:
            lines = f.readlines()
            svg = ''.join(lines)
        filename = to_image(svg, 'gif', 200)
        self.assertRegex(filename, r'.\.gif')
        os.remove(STATIC_DIR % re.search(r'[\w\d]+.gif', filename).group(0))

    def test_create_image_bad_svg(self):
        with open('mathml_to_image_service/tests/broken.svg') as f:
            lines = f.readlines()
            svg = ''.join(lines)
        with self.assertRaises(ImageConvertError) as e:
            filename = to_image(svg, 'png', 200)
        self.assertEqual(
            e.exception.args[0],
            'Invalid SVG')

    def test_create_bad_format_parameter(self):
        with open('mathml_to_image_service/tests/mathoid_test_data.svg') as f:
            lines = f.readlines()
            svg = ''.join(lines)
        with self.assertRaises(NameError) as e:
            filename = to_image(svg, 'foo', 200)
        self.assertEqual(
            e.exception.args[0],
            'Unsupported output file format - "GIF" and "PNG" only.')

    def test_create_quality_2_png(self):
        with open('mathml_to_image_service/tests/mathoid_test_data.svg') as f:
            lines = f.readlines()
            svg = ''.join(lines)
        filename = to_image(svg, 'png', 200, 2)
        self.assertRegex(filename, r'.\.png')
        os.remove(STATIC_DIR % re.search(r'[\w\d]+.png', filename).group(0))

    def test_create_quality_1_png(self):
        with open('mathml_to_image_service/tests/mathoid_test_data.svg') as f:
            lines = f.readlines()
            svg = ''.join(lines)
        filename = to_image(svg, 'png', 200, 1)
        self.assertRegex(filename, r'.\.png')
        os.remove(STATIC_DIR % re.search(r'[\w\d]+.png', filename).group(0))

    def test_create_quality_2_gif(self):
        with open('mathml_to_image_service/tests/mathoid_test_data.svg') as f:
            lines = f.readlines()
            svg = ''.join(lines)
        filename = to_image(svg, 'gif', 200, 2)
        self.assertRegex(filename, r'.\.gif')
        os.remove(STATIC_DIR % re.search(r'[\w\d]+.gif', filename).group(0))

    def test_create_quality_1_gif(self):
        with open('mathml_to_image_service/tests/mathoid_test_data.svg') as f:
            lines = f.readlines()
            svg = ''.join(lines)
        filename = to_image(svg, 'gif', 200, 1)
        self.assertRegex(filename, r'.\.gif')
        os.remove(STATIC_DIR % re.search(r'[\w\d]+.gif', filename).group(0))
