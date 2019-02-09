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

        self.party =   {
        "id": 5,
        "name": "Democratic Party",
        "hqAddress": "Nyeri",
        "logoUrl": "/dp.png"
    }
        

    

    def test_posting_party_list(self):
        resp = self.client.post(path='api/v1/party', data=json.dumps(self.party), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
    
    def test_getting_party_list(self):
        resp = self.client.get(path='api/v1/party', content_type='application/json')
        self.assertEqual(resp.status_code, 200)
