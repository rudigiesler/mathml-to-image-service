import unittest
from mathoid_client import get_svg


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

if __name__ == '__main__':
    unittest.main()
