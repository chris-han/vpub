import unittest
import app
import os
import base64
import json
import tempfile
from flask import Flask
from flask.testing import FlaskClient

class TestApp(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_get_item(self):
        json_list = [{'ps': 'item1', 'value': 1}, {'ps': 'item2', 'value': 2}]
        ps = 'item1'
        expected_output = {'ps': 'item1', 'value': 1}
        self.assertEqual(app.get_item(json_list, ps), expected_output)

    def test_load_v2ray_config(self):
        # Create a temporary file with base64-encoded JSON data
        temp_file_path = os.path.join(tempfile.gettempdir(), 'v2ray_config4.json')
        json_data = [{'ps': 'item1', 'value': 1}, {'ps': 'item2', 'value': 2}]
        b64_json = base64.b64encode(json.dumps(json_data).encode())
        with open(temp_file_path, 'wb') as f:
            f.write(b64_json)

        # Call the function and check the output
        expected_output = json_data
        self.assertEqual(app.load_v2ray_config(), expected_output)

        # Remove the temporary file
        os.remove(temp_file_path)

    def test_get_servers(self):
        # Create a temporary file with base64-encoded JSON data
        temp_file_path = os.path.join(tempfile.gettempdir(), 'v2ray_config4.json')
        json_data = [{'ps': 'item1', 'value': 1}, {'ps': 'item2', 'value': 2}]
        b64_json = base64.b64encode(json.dumps(json_data).encode())
        with open(temp_file_path, 'wb') as f:
            f.write(b64_json)

        # Call the function and check the output
        expected_output = 'vmess://' + base64.b64encode(json.dumps(json_data[0]).encode()).decode() + '\n' + 'vmess://' + base64.b64encode(json.dumps(json_data[1]).encode()).decode() + '\n'
        self.assertEqual(app.get_servers(), expected_output)

        # Remove the temporary file
        os.remove(temp_file_path)

    def test_updateip(self):
        # Create a test client


        response = self.client.get('/updateip?addr=192.168.1.1&loc=NYC')
        self.assertEqual(response.status_code, 200)

        # Test with missing parameters
        response = self.client.get('/updateip')
        self.assertEqual(response.status_code, 400)

        # Test with invalid IP address
        response = self.client.get('/updateip?addr=invalid&loc=NYC')
        self.assertEqual(response.status_code, 400)

        # Test with invalid location
        response = self.client.get('/updateip?addr=192.168.1.1&loc=invalid')
        self.assertEqual(response.status_code, 400)