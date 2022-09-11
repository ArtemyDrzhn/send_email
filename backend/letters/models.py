# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Subscribers(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    birthday = models.DateField()

    def __str__(self):
        return self.name + ' ' + self.surname


class TrackedEmail(models.Model):
    email = models.EmailField()
    message_id = models.CharField(max_length=36)
    status = models.CharField(max_length=9)
    timestamp = models.DateTimeField()
