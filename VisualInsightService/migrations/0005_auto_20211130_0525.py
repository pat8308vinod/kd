# Generated by Django 3.2.5 on 2021-11-30 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisualInsightService', '0004_topfeature_featureid'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuretype',
            name='featureUnit',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='topfeature',
            name='significance',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]
