# Generated by Django 4.1.3 on 2022-12-03 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_rename_massege_messege'),
    ]

    operations = [
        migrations.AddField(
            model_name='messege',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='messege',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 14, 54, 32, 618151, tzinfo=datetime.timezone.utc)),
        ),
    ]
