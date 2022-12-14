# Generated by Django 3.2.5 on 2021-12-20 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SummaryDXIInsightService', '0011_summaryinsights_allappdownloads'),
        ('KeydabraManagerController', '0001_initial'),
        ('TransactionService', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CNNRecommender',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=250)),
                ('similarityScore', models.IntegerField(null=True)),
                ('parentImageID', models.IntegerField(null=True)),
                ('collateralID', models.ForeignKey(db_column='collateralID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='SummaryDXIInsightService.collateral')),
                ('reportID', models.ForeignKey(db_column='reportID', on_delete=django.db.models.deletion.CASCADE, to='KeydabraManagerController.report')),
            ],
            options={
                'db_table': 'CNNRecommender',
            },
        ),
    ]
