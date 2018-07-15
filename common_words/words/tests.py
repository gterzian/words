# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import mock
from django.test import TransactionTestCase

from .models import Word


class PatchedResponse(object):
    @property
    def text(self):
        return '''<html><body><p>The <b>2018 FIFA World Cup</b> is the 21st
        <a href="/wiki/FIFA_World_Cup" title="FIFA World Cup">FIFA World Cup</a>,
        an international <a href="/wiki/Association_football" title="Association football">football</a>
        tournament contested by the <a href="/wiki/List_of_men%27s_national_association_football_teams"
        title="List of men's national association football teams">men's national teams</a> of the member associations
        of <a href="/wiki/FIFA" title="FIFA">FIFA</a> once every four years. It is currently ongoing in
        <a href="/wiki/Russia" title="Russia">Russia</a> starting from 14 June and will end with the
        final match on 15 July 2018.<sup id="cite_ref-press_release_1-0" class="reference">
        <a href="#cite_note-press_release-1">[1]</a></sup></p></body></html>'''


class PatchedRequest(object):
    def get(self, url):
        return PatchedResponse()


class TestViews(TransactionTestCase):

    def test_delete_search_result(self):
        data = dict(url="https://en.wikipedia.org/wiki/2018_FIFA_World_Cup")
        with mock.patch('common_words.words.views.requests', new=PatchedRequest()):
            response = self.client.post("/", json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            fifa = Word.objects.get(word='FIFA')
            self.assertEqual(fifa.occurences, 3)
