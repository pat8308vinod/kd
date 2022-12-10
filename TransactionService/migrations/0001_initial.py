# Generated by Django 3.2.5 on 2021-09-21 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('KeydabraManagerController', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionSummary',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('transactions', models.IntegerField(null=True)),
                ('income', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('itemsInPurchase', models.IntegerField(null=True)),
                ('avgSizeOfPurchase', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('isApproved', models.BooleanField(null=True)),
                ('approvedBy', models.CharField(max_length=50)),
                ('reportID', models.ForeignKey(db_column='reportID', on_delete=django.db.models.deletion.CASCADE, to='KeydabraManagerController.report')),
            ],
            options={
                'db_table': 'TransactionSummary',
            },
        ),
        migrations.CreateModel(
            name='TopProduct',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(null=True)),
                ('reportID', models.ForeignKey(db_column='reportID', on_delete=django.db.models.deletion.CASCADE, to='KeydabraManagerController.report')),
            ],
            options={
                'db_table': 'TopProduct',
            },
        ),
    ]
