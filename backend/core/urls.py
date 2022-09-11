from django.conf.urls import url
from django.contrib import admin

from letters.views import HomeView, send

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'send/', send, name='send'),
    url(r'^admin/', admin.site.urls, name='admin'),
]
