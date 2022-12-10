# Generated by Django 3.2.5 on 2021-09-02 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('KeydabraManagerController', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummaryInsights',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('month', models.CharField(max_length=15)),
                ('DXI', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('TargetDXI', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('currentConversionRate', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('targetConversionRate', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('GAConversionRate', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('visitors', models.IntegerField(null=True)),
                ('uniqueBuyers', models.IntegerField(null=True)),
                ('transactions', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('prospectiveBuyers', models.IntegerField(null=True)),
                ('netDollarValue', models.DecimalField(decimal_places=3, max_digits=10)),
                ('topDXIConversionRate', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('lowDXIConversionRate', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('reportID', models.ForeignKey(db_column='reportID', on_delete=django.db.models.deletion.CASCADE, to='KeydabraManagerController.report')),
            ],
            options={
                'db_table': 'SummaryInsights',
            },
        ),
        migrations.CreateModel(
            name='Statements',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('statementType', models.CharField(choices=[('INFER', 'Inference'), ('OBSER', 'Observation'), ('PRED', 'Prediction'), ('RECOM', 'Recommendation')], max_length=10)),
                ('statementSubtype', models.CharField(max_length=10, null=True)),
                ('informationType', models.CharField(max_length=30)),
                ('statementText', models.TextField(max_length=500)),
                ('solutionText', models.TextField(max_length=500, null=True)),
                ('isApproved', models.BooleanField()),
                ('approvedBy', models.CharField(max_length=50)),
                ('reportID', models.ForeignKey(db_column='reportID', on_delete=django.db.models.deletion.CASCADE, to='KeydabraManagerController.report')),
            ],
            options={
                'db_table': 'Statements',
            },
        ),
    ]
