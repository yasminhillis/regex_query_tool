# Generated by Django 3.1.2 on 2020-10-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regextool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='avres',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='tool',
            name='regex',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='tool',
            name='text',
            field=models.CharField(default='null', max_length=500),
        ),
    ]
