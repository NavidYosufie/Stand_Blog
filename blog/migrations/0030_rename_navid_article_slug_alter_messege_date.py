# Generated by Django 4.1.3 on 2023-01-01 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_rename_slug_article_navid_alter_messege_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='navid',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='messege',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 1, 17, 31, 8, 462717, tzinfo=datetime.timezone.utc)),
        ),
    ]
