# Generated by Django 2.1.2 on 2018-10-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Infodate', '0008_auto_20181029_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='infodate',
            name='date_brake_last',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='infodate',
            name='date_liq_last',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='infodate',
            name='date_to_last',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='infodate',
            name='date_create',
            field=models.DateField(),
        ),
    ]
