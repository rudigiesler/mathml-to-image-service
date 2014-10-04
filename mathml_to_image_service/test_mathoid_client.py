import unittest
from mathoid_client import get_svg


class MathoidTestCase(unittest.TestCase):
    def setUp(self):
        with open('mathml_to_image_service/mathoid_test_data.svg') as f:
            lines = f.readlines()
            self.data = ''.join(lines)

    def test_basic_encode(self):
        self.assertEqual(get_svg('<math><mi>x</mi></math>'), self.data)

if __name__ == '__main__':
    unittest.main()
