# Generated by Django 3.1.1 on 2021-01-01 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0017_auto_20200912_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='img',
        ),
        migrations.RemoveField(
            model_name='log',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
