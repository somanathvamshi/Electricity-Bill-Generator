# Generated by Django 3.1.6 on 2021-04-25 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elc_bill', '0007_auto_20210425_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='state',
        ),
    ]