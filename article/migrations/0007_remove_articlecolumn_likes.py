# Generated by Django 3.0 on 2022-04-06 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_articlecolumn_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecolumn',
            name='likes',
        ),
    ]
