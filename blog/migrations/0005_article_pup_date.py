# Generated by Django 4.0.6 on 2022-09-01 15:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_body_alter_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pup_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 1, 15, 20, 51, 358143, tzinfo=utc)),
        ),
    ]
