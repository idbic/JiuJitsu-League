# Generated by Django 4.0.6 on 2022-07-27 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_tournaments_athletes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournaments',
            name='prices',
        ),
    ]