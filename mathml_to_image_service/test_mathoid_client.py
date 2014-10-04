import unittest
from mathoid_client import get_svg, SVGEncodeError


class MathoidTestCase(unittest.TestCase):
    def setUp(self):
        with open('mathml_to_image_service/mathoid_test_data.svg') as f:
            lines = f.readlines()
            self.svg = ''.join(lines)
        with open('mathml_to_image_service/mathoid_test_data.mml') as f:
            lines = f.readlines()
            self.mml = ''.join(lines)

    def test_basic_encode(self):
        self.assertEqual(get_svg(self.mml), self.svg)

    def test_broken_encode(self):
        with self.assertRaises(SVGEncodeError):
            get_svg('<math>')
            get_svg('<foo></foo>')

if __name__ == '__main__':
    unittest.main()
