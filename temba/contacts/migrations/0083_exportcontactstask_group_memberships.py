# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-19 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("contacts", "0082_auto_20180615_2040")]

    operations = [
        migrations.AddField(
            model_name="exportcontactstask",
            name="group_memberships",
            field=models.ManyToManyField(to="contacts.ContactGroup"),
        )
    ]
