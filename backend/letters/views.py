# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.views.generic import TemplateView

from letters.tasks import send_letter


class HomeView(TemplateView):
    template_name = 'letters/home.html'


def send(request):
    send_letter.delay()
    return redirect('home')
