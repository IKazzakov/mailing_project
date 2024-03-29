
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import HomePageView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, set_mailing_active, \
    MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingLogListView

app_name = MailingConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    path('mailing_list', MailingListView.as_view(), name='mailing_list'),
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('mailing_log_list/', MailingLogListView.as_view(), name='mailing_log_list'),

    path('set_mailing_active/<int:pk>', login_required(set_mailing_active), name='set_mailing_active')

]
