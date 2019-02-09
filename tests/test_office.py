import os , unittest
import json, requests, pytest
import app
import os
from flask import jsonify , request



class TestOffice(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app =app.create_app()
        self.client = self.app.test_client()

        self.office_1 = {
        "id": 6,
        "type": "County Type",
        "office": "Gubernatorial Office"
        }
        self.office_2 = {
        "id": 7,
        "type": "County Type",
        "office": "Senator's Office"
         }

    

    def test_posting_office_list(self):
        resp = self.client.post(path='api/v1/office', data=json.dumps(self.office_1), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
    
    def test_getting_office_list(self):
        resp = self.client.get(path='api/v1/office', content_type='application/json')
        self.assertEqual(resp.status_code, 200
        )
    
   