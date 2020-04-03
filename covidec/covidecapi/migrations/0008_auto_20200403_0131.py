# Generated by Django 3.0.4 on 2020-04-03 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covidecapi', '0007_auto_20200402_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pais',
            name='provincias',
        ),
        migrations.AddField(
            model_name='pais',
            name='pvs',
            field=models.ManyToManyField(related_name='pvs', to='covidecapi.Provincia'),
        ),
        migrations.AlterField(
            model_name='casocovid',
            name='fk_pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paises', to='covidecapi.Pais'),
        ),
        migrations.AlterField(
            model_name='casocovid',
            name='fk_provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provincias', to='covidecapi.Provincia'),
        ),
    ]
