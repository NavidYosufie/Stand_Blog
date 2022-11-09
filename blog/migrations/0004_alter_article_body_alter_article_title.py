# Generated by Django 4.0.6 on 2022-09-01 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(choices=[('a', 'python'), ('b', 'django')], max_length=90, unique=True),
        ),
    ]
