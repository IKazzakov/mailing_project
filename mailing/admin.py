from django.contrib import admin

from mailing.models import Client, Message, Mailing, MailingLog


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'comment', 'user')
    search_fields = ('email', 'full_name')
    list_filter = ('user',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', 'user')
    search_fields = ('subject', 'body')
    list_filter = ('user',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('mailing_date', 'mailing_time', 'frequency', 'mailing_status', 'user', 'is_active')
    search_fields = ('mailing_date', 'mailing_time', 'frequency', 'mailing_status')
    list_filter = ('user', 'is_active')


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'server_response', 'attempt_time', 'status')
    search_fields = ('mailing', 'server_response', 'status')
    list_filter = ('mailing', 'server_response', 'status')
