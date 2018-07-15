# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.test import TransactionTestCase


class TestViews(TransactionTestCase):

    def test_delete_search_result(self):
        data = dict(url="https://en.wikipedia.org/wiki/2018_FIFA_World_Cup")
        response = self.client.post("/", json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)