# Generated by Django 3.0.4 on 2020-03-17 15:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='year_released',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 17, 15, 29, 27, 724429, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
