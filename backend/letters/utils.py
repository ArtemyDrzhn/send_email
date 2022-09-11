# coding=utf-8
from __future__ import unicode_literals

import requests
from django.conf import settings

from letters.models import Subscribers


def get_letter_data():
    subscribers = Subscribers.objects.all()
    result = list()
    for user in subscribers:
        result.append(
            {
                'name': user.name + ' ' + user.surname,
                'birthday': user.birthday.strftime('%d.%m.%Y'),
            }
        )
    return result


def get_data_log():
    return requests.get('https://api.mailgun.net/v3/%s/events' % settings.MAILGUN_SERVER_NAME,
                        auth=('api', settings.MAILGUN_ACCESS_KEY))
