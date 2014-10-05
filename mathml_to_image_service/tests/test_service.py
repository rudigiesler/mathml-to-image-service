import json
import os
import re
import unittest

from config import STATIC_DIR

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

    def test_root_path_post_400_bad_mathml(self):
        response = self.app.post(
            '/', data={'mathml': '<math>', 'image_format': 'png',
                       'max_size': '300'})
        self.assertEqual(
            json.loads(response.data.decode('utf-8')),
            {'error': 'Invalid MathML no element found: line 1, column 6'})
        self.assertEqual(response.status_code, 400)

    def test_root_path_post_redirect_to_image(self):
        response = self.app.post(
            '/', data={'mathml': '<math></math>', 'image_format': 'png',
                       'max_size': '300'})
        data = json.loads(response.data.decode('utf-8'))
        self.assertIn('url', data)
        self.assertRegex(data.get('url'), r'[\w\d]+.png')
        os.remove(
            STATIC_DIR % re.search(r'[\w\d]+.png', data.get('url')).group(0))


if __name__ == '__main__':
    unittest.main()
