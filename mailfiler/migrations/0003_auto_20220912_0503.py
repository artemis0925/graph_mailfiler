# Generated by Django 3.2.15 on 2022-09-12 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailfiler', '0002_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='immutableId',
            field=models.CharField(max_length=266),
        ),
        migrations.AlterField(
            model_name='mail',
            name='sender',
            field=models.CharField(max_length=266),
        ),
        migrations.AlterField(
            model_name='mail',
            name='subject',
            field=models.CharField(max_length=266),
        ),
    ]
