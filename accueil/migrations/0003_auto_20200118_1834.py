# Generated by Django 2.0.13 on 2020-01-18 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0002_sujet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sujet',
        ),
        migrations.AlterModelOptions(
            name='accueil',
            options={'ordering': ['date'], 'verbose_name': 'article'},
        ),
        migrations.RenameField(
            model_name='accueil',
            old_name='message_accueil',
            new_name='item',
        ),
    ]
