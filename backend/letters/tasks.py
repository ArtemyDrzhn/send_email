# coding=utf-8
from __future__ import unicode_literals

import datetime
import json

import pytz
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from core.celery_app import app
from letters.models import TrackedEmail
from letters.utils import get_letter_data, get_data_log


@app.task
def send_letter():
    data = get_letter_data()
    rendered = render_to_string('letters/letter.html', {'users': data})
    plain_message = strip_tags(rendered)
    send_mail(subject='Subject', message=plain_message, from_email=settings.EMAIL_FROM,
              recipient_list=[settings.EMAIL_TO],
              html_message=rendered)


@app.task
def get_logs():
    data = get_data_log()
    items = json.loads(data.content)['items']
    for item in items:
        TrackedEmail.objects.update_or_create(email=item['recipient'],
                                              message_id=item['message']['headers']['message-id'],
                                              status=item['event'],
                                              timestamp=datetime.datetime.fromtimestamp(item['timestamp'],
                                                                                        tz=pytz.timezone(
                                                                                            settings.TIME_ZONE)))
