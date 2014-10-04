import json
import unittest

import service


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = service.app.test_client()

    def test_root_path(self):
        self.assertEqual(
            json.loads(self.app.get('/').data.decode('utf-8')),
            {'error': 'Try sending MathML in a POST request. :)'})

if __name__ == '__main__':
    unittest.main()
