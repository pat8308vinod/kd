# Generated by Django 3.2.5 on 2022-01-19 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BehavioralInsightService', '0004_clusterdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clusterdata',
            old_name='sliceName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='clusterdata',
            old_name='sliceScore',
            new_name='score',
        ),
        migrations.AddField(
            model_name='clusterdata',
            name='metaInfo',
            field=models.CharField(max_length=35, null=True),
        ),
    ]
