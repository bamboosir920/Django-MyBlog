# Generated by Django 3.0 on 2022-04-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_remove_articlecolumn_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='avatar',
            field=models.URLField(default='https://s1.ax1x.com/2022/04/11/LEjUYV.jpg'),
        ),
    ]
