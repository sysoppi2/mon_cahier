# Generated by Django 2.0.13 on 2019-10-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maison', '0006_auto_20191029_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
