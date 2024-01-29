
from django.contrib import admin
from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import test_page

app_name = MailingConfig.name

urlpatterns = [
    path('', test_page, name='test_page'),
]
