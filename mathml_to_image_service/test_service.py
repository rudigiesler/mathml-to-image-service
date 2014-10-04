import unittest

import service


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = service.app.test_client()

    def test_root_path(self):
        self.assertEqual(self.app.get('/').data, b'Hello World!')

if __name__ == '__main__':
    unittest.main()
