# Generated by Django 3.0 on 2022-04-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0003_auto_20220412_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuscriptspost',
            name='baidu_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='manuscriptspost',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]