# Generated by Django 2.0.13 on 2020-02-01 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mon_django', '0004_mondjango_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mondjango',
            name='slug',
        ),
    ]
