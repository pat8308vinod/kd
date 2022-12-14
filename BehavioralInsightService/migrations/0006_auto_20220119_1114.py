# Generated by Django 3.2.5 on 2022-01-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BehavioralInsightService', '0005_auto_20220119_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clusterdata',
            name='metaInfo',
            field=models.CharField(default='Good Cluster', max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='clusterdata',
            name='score',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]
