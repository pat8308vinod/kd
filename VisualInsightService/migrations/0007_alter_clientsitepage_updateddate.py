# Generated by Django 3.2.5 on 2022-01-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisualInsightService', '0006_alter_clientsitepage_pagereferenceid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsitepage',
            name='updatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
