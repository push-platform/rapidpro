# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-10 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triggers', '0010_auto_20170509_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trigger',
            name='trigger_type',
            field=models.CharField(choices=[('K', 'Keyword Trigger'), ('S', 'Schedule Trigger'), ('V', 'Inbound Call Trigger'), ('M', 'Missed Call Trigger'), ('C', 'Catch All Trigger'), ('F', 'Follow Account Trigger'), ('N', 'New Conversation Trigger'), ('U', 'USSD Pull Session Trigger'), ('R', 'Referral Trigger'), ('L', 'NLU API Trigger')], default='K', help_text='The type of this trigger', max_length=1, verbose_name='Trigger Type'),
        ),
    ]
