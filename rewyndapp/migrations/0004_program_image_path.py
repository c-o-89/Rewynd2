# Generated by Django 2.0.1 on 2018-09-08 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewyndapp', '0003_auto_20180901_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='image_path',
            field=models.CharField(default='placeholder.jpeg', max_length=200),
        ),
    ]
