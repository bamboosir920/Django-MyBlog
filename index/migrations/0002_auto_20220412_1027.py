# Generated by Django 3.0 on 2022-04-12 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeriesBg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.URLField(default='https://s1.ax1x.com/2022/04/11/LEjUYV.jpg')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageShow',
        ),
    ]
