# Generated by Django 3.2.5 on 2021-12-01 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KeyDataService', '0002_auto_20211016_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('population', models.IntegerField(null=True)),
                ('avgAge', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('avgIncome', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'Location',
            },
        ),
    ]