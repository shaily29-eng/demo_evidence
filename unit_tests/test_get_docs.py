import unittest
import requests

class TestGetDocs(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://3.82.58.102:8000/get_docs'
        self.headers = {'accept': 'application/json'}

    def test_status_code(self):
        params = {'user_id': 'any_string'}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        self.assertEqual(response.status_code, 200)

    def test_content_type(self):
        params = {'user_id': 'any_string'}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_response_structure(self):
        params = {'user_id': 'any_string'}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        response_data = response.json()
        
        # Assert basic structure of the response
        self.assertIn('user_id', response_data)
        self.assertIn('doc_pages', response_data)
        self.assertIsInstance(response_data['doc_pages'], list)
        
        if response_data['doc_pages']:
            first_doc = response_data['doc_pages'][0]
            self.assertIn('doc_name', first_doc)
            self.assertIn('pages', first_doc)
            self.assertIsInstance(first_doc['pages'], list)
            self.assertGreater(len(first_doc['pages']), 0)

    def test_response_content(self):
        params = {'user_id': 'any_string'}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        response_data = response.json()

        # Assert content of the response
        self.assertIn('user_id', response_data)
        self.assertIn('doc_pages', response_data)
        self.assertIsInstance(response_data['doc_pages'], list)
        
        if response_data['doc_pages']:
            first_doc = response_data['doc_pages'][0]
            self.assertIn('doc_name', first_doc)
            self.assertIn('pages', first_doc)
            self.assertIsInstance(first_doc['pages'], list)
            self.assertGreater(len(first_doc['pages']), 0)

if __name__ == '__main__':
    unittest.main()

