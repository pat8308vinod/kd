# Generated by Django 3.2.5 on 2021-11-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SummaryDXIInsightService', '0007_auto_20211020_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='statements',
            name='overviewFlag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='statements',
            name='isApproved',
            field=models.BooleanField(default=False),
        ),
    ]
