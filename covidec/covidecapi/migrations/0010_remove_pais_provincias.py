# Generated by Django 3.0.4 on 2020-04-03 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covidecapi', '0009_auto_20200403_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pais',
            name='provincias',
        ),
    ]
