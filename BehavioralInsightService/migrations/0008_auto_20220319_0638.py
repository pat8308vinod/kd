# Generated by Django 3.2.5 on 2022-03-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BehavioralInsightService', '0007_alter_clusterdata_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='clusterdata',
            name='reportName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reviewsentiment',
            name='reportName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='wordcloud',
            name='reportName',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
