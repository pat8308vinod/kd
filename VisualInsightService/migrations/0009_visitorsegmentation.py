# Generated by Django 3.2.5 on 2022-01-25 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KeydabraManagerController', '0003_auto_20220108_0542'),
        ('VisualInsightService', '0008_featuresuggestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorSegmentation',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('userID', models.CharField(max_length=20, null=True)),
                ('significance', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('compositeDXI', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('userRank', models.IntegerField(null=True)),
                ('metaInfo', models.CharField(max_length=70, null=True)),
                ('featureID', models.ForeignKey(db_column='featureID', on_delete=django.db.models.deletion.CASCADE, to='VisualInsightService.featuretype')),
                ('reportID', models.ForeignKey(db_column='reportID', on_delete=django.db.models.deletion.CASCADE, to='KeydabraManagerController.report')),
            ],
            options={
                'db_table': 'VisitorSegmentation',
            },
        ),
    ]
