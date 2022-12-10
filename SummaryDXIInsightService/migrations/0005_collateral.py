# Generated by Django 3.2.5 on 2021-10-02 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KeydabraManagerController', '0001_initial'),
        ('SummaryDXIInsightService', '0004_alter_statements_statementtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collateral',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('typeName', models.CharField(max_length=35, null=True)),
                ('typeID', models.IntegerField(null=True)),
                ('collateralMimeType', models.CharField(max_length=8)),
                ('collateralContent', models.BinaryField()),
                ('reportID', models.ForeignKey(db_column='reportID', on_delete=django.db.models.deletion.CASCADE, to='KeydabraManagerController.report')),
            ],
            options={
                'db_table': 'Collateral',
            },
        ),
    ]