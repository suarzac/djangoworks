# Generated by Django 3.2.3 on 2021-06-02 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0002_auto_20210528_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]
