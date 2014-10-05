import json
import unittest

from mathml_to_image_service import service


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = service.app.test_client()

    def test_root_path_get(self):
        self.assertEqual(
            json.loads(self.app.get('/').data.decode('utf-8')),
            {'error': 'Try sending MathML in a POST request. :)'})

    def test_root_path_post_400_with_missing_field(self):
        response = self.app.post('/')
        self.assertEqual(
            json.loads(response.data.decode('utf-8')),
            {'error': 'Missing field: mathml'})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
