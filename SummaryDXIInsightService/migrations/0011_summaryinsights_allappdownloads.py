# Generated by Django 3.2.5 on 2021-12-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SummaryDXIInsightService', '0010_auto_20211206_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='summaryinsights',
            name='allAppDownloads',
            field=models.IntegerField(null=True),
        ),
    ]