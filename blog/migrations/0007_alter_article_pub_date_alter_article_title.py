# Generated by Django 4.0.6 on 2022-09-01 15:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_article_pup_date_article_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 1, 15, 28, 32, 514318, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(choices=[('a', 'python'), ('b', 'django'), ('c', 'flask')], default='a', max_length=90, unique_for_date='pub_date'),
        ),
    ]
