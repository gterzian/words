# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse

def process_url(request):
    data = json.loads(request.body)
    return HttpResponse('OK')
