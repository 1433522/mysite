# Generated by Django 3.1.1 on 2020-09-12 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0016_auto_20200910_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='tags',
            field=models.ManyToManyField(blank=True, to='diary.Tag'),
        ),
    ]
