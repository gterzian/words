# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import HTMLParser
import collections
import json

import requests
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Word


class Parser(HTMLParser.HTMLParser):

    words = []

    def handle_data(self, data):
        for word in data.split(' '):
            if word:
                self.words.append(word)

    def get_most_common_words(self, num):
        word_counts = collections.Counter(self.words)
        for (word, count) in word_counts.most_common(num):
            yield Word(word=word, occurences=count)


@require_http_methods(["POST"])
def process_url(request):
    data = json.loads(request.body)
    r = requests.get(data['url'])
    parser = Parser()
    parser.feed(r.text)
    most_common = parser.get_most_common_words(100)
    Word.objects.bulk_create(most_common)
    parser.close()
    return HttpResponse('OK')
