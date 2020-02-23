# Generated by Django 2.0.13 on 2019-10-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maison', '0002_auto_20191027_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
