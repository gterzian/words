# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=200, null=True, unique=True)
    occurences = models.IntegerField(null=True)
