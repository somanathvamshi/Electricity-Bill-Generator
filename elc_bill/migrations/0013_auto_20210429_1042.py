# Generated by Django 3.1.6 on 2021-04-29 05:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('elc_bill', '0012_auto_20210425_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='date',
            new_name='from_date',
        ),
        migrations.AddField(
            model_name='details',
            name='to_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 4, 29, 5, 12, 3, 864910, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='gender',
            field=models.CharField(max_length=40),
        ),
    ]
