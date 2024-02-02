from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.EmailField(max_length=100, unique=True, verbose_name='email')
    full_name = models.CharField(max_length=100, verbose_name='full name')
    comment = models.TextField(verbose_name='comment', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)

    def __str__(self):
        return f'{self.email} - {self.full_name}'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='Email subject')
    body = models.TextField(verbose_name="Message's text")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class Mailing(models.Model):
    FREQUENCY_CHOICES = [
        ('DAILY', 'daily'),
        ('WEEKLY', 'weekly'),
        ('MONTHLY', 'monthly'),
    ]

    STATUS_CHOICES = [
        ('CREATED', 'created'),
        ('STARTED', 'started'),
        ('FINISHED', 'finished')
    ]

    mailing_date = models.DateTimeField(verbose_name='mailing date', default=timezone.now)
    mailing_time = models.TimeField(verbose_name='mailing time')
    frequency = models.CharField(max_length=50, verbose_name='frequency', choices=FREQUENCY_CHOICES)
    mailing_status = models.CharField(max_length=50, verbose_name='mailing status', choices=STATUS_CHOICES, default='CREATED')

    clients = models.ManyToManyField(Client, verbose_name='Clients for mailing')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Message')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='is active?')

    def __str__(self):
        return f'ID: {self.id}, user: {self.user}'

    class Meta:
        verbose_name = 'mailing'
        verbose_name_plural = 'mailing'
        permissions = [
            (
                'set_mailing_active',
                'Can set mailing active'
            ),
        ]


class MailingLog(models.Model):
    STATUS_CHOICES = [
        ('SENT', 'sent'),
        ('FAILED', 'failed'),
        ('PENDING', 'pending')
    ]

    attempt_time = models.DateTimeField(auto_now_add=True ,verbose_name='time of attempt')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='status of attempt')
    server_response = models.TextField(max_length=200, verbose_name='server response')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='mailing')

    def __str__(self):
        return f'Log for {self.mailing.id}'

    class Meta:
        verbose_name = 'Mailing log'
        verbose_name_plural = 'Mailing logs'
