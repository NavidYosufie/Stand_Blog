# Generated by Django 4.1.2 on 2022-10-15 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'post'},
        ),
        migrations.AddField(
            model_name='cateqory',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
