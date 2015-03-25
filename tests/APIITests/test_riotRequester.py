
__author__ = 'Netwave'

from unittest import TestCase
from unittest.mock import Mock
from code.APIInterface.Requester import *

class TestRiotRequester(TestCase):
    def test_test(self):
        test_data = {"n3twave": {"id": 39600108,
                                 "name": "N3twave",
                                 "profileIconId": 662,
                                 "revisionDate": 1427293639000,
                                 "summonerLevel": 30}}
        m = Mock()
        m.get.return_value = m
        m.json.return_value = test_data
        r = RiotRequester(m)
        response = r.test(RiotRequester.europewest)
        self.assertEqual(response, test_data)

    def test_getUserHistory(self):
        test_data = {"status": {"status_code": 503, "message": "Service unavailable"}}
        m = Mock()
        m.get.return_value = m
        m.json.return_value = test_data
        r = RiotRequester(m)
        response = r.getUserHistory("n3twave", 1, RiotRequester.europewest)
        self.assertEqual(response, test_data)