# Generated by Django 3.0.4 on 2020-04-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidecapi', '0004_remove_casocovid_fecha_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casocovid',
            name='activos',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='casocovid',
            name='confirmados',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='casocovid',
            name='muertos',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='casocovid',
            name='nuevos',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='casocovid',
            name='recuperados',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='casocovid',
            name='total',
            field=models.FloatField(),
        ),
    ]
