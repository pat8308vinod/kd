# Generated by Django 3.2.5 on 2022-01-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientManagementService', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='companyID',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
