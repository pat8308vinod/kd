# Generated by Django 3.2.5 on 2022-03-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KeydabraManagerController', '0003_auto_20220108_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reportName',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='report',
            unique_together={('ID', 'reportName')},
        ),
    ]
