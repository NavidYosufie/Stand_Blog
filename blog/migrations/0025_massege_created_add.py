# Generated by Django 4.1.3 on 2022-11-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_massege'),
    ]

    operations = [
        migrations.AddField(
            model_name='massege',
            name='created_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
