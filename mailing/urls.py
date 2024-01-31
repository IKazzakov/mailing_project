
from django.contrib import admin
from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import HomePageView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
