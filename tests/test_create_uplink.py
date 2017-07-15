import unittest
from unittest.mock import patch, MagicMock

import requests
import app

from flask import json
from samples.create_uplink import *
from actions.api import SteelConnectAPI

class TestCreateUplinks(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_melbourne_shop_success(self):
        mock_api =  SteelConnectAPI("Aubrey","Aubrey",'monash.riverbed.cc','org-Monash-d388075e40cf1bfd')
        mock_api.create_uplink = MagicMock(name="create_uplink")
        mock_api.create_uplink.return_value = MagicMock(spec=requests.Response, status_code=200)
        result = app.create_uplink(mock_api, melbourne_shop_parameters)
        self.assertTrue(mock_api.create_uplink.called)
        self.assertEqual(melbourne_shop_success_speech_response, result)

    def test_melbourne_shop_400(self):
        mock_api = SteelConnectAPI("Aubrey", "Aubrey", 'monash.riverbed.cc', 'org-Monash-d388075e40cf1bfd')
        mock_api.create_uplink = MagicMock(name="create_uplink")
        mock_api.create_uplink.return_value = MagicMock(spec=requests.Response, status_code=400)
        mock_api.create_uplink.return_value.json.return_value = melbourne_shop_400_api_response
        result = app.create_uplink(mock_api, melbourne_shop_parameters)
        self.assertTrue(mock_api.create_uplink.called)
        self.assertEqual(melbourne_shop_400_speech_response, result)

    def test_melbourne_shop_500(self):
        mock_api =  SteelConnectAPI("Aubrey","Aubrey",'monash.riverbed.cc','org-Monash-d388075e40cf1bfd')
        mock_api.create_uplink = MagicMock(name="create_uplink")
        mock_api.create_uplink.return_value = MagicMock(spec=requests.Response, status_code=500)
        result = app.create_uplink(mock_api, melbourne_shop_parameters)
        self.assertTrue(mock_api.create_uplink.called)
        self.assertEqual(melbourne_shop_500_speech_response, result)

    def test_melbourne_shop_404(self):
        mock_api = SteelConnectAPI("Aubrey", "Aubrey", 'monash.riverbed.cc', 'org-Monash-d388075e40cf1bfd')
        mock_api.create_uplink = MagicMock(name="create_uplink")
        mock_api.create_uplink.return_value = MagicMock(spec=requests.Response, status_code=404)
        result = app.create_uplink(mock_api, melbourne_shop_parameters)
        self.assertTrue(mock_api.create_uplink.called)
        self.assertEqual(melbourne_shop_404_speech_response, result)

    def test_invalid_site(self):
        mock_api = SteelConnectAPI("Aubrey", "Aubrey", 'monash.riverbed.cc', 'org-Monash-d388075e40cf1bfd')
        mock_api.create_uplink = MagicMock(name="create_uplink")
        result = app.create_uplink(mock_api, tokyo_branch_parameters)
        mock_api.create_uplink.return_value = MagicMock(invalid_site_speech_response)
        self.assertTrue(mock_api.create_uplink.called)
        self.assertEqual(invalid_site_speech_response, result)

    def test_invalid_wan(self):
        mock_api = SteelConnectAPI("Aubrey", "Aubrey", 'monash.riverbed.cc', 'org-Monash-d388075e40cf1bfd')
        mock_api.create_uplink = MagicMock(name="create_uplink")
        result = app.create_uplink(mock_api, hahawan_parameters)
        mock_api.create_uplink.return_value = MagicMock(invalid_wan_speech_response)
        self.assertTrue(mock_api.create_uplink.called)
        self.assertEqual(invalid_wan_speech_response, result)