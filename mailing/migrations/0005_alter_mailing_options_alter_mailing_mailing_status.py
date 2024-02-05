# Generated by Django 4.2.9 on 2024-02-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_alter_mailing_is_active_alter_mailing_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'permissions': [('set_mailing_active', 'Can set mailing active')], 'verbose_name': 'mailing', 'verbose_name_plural': 'mailing'},
        ),
        migrations.AlterField(
            model_name='mailing',
            name='mailing_status',
            field=models.CharField(choices=[('CREATED', 'created'), ('STARTED', 'started'), ('FINISHED', 'finished')], default='CREATED', max_length=50, verbose_name='mailing status'),
        ),
    ]
