# Generated by Django 4.0.6 on 2022-10-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_article_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
