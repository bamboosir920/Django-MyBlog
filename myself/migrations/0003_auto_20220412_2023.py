# Generated by Django 3.0 on 2022-04-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myself', '0002_auto_20220412_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendlink',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
