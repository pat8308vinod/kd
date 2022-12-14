# Generated by Django 3.2.5 on 2021-10-07 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('KeydabraManagerController', '0001_initial'),
        ('ClientManagementService', '0001_initial'),
        ('KeyDataService', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientSitePage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pageName', models.CharField(max_length=200, null=True)),
                ('pageReferenceID', models.IntegerField()),
                ('updatedDate', models.DateTimeField(auto_now_add=True)),
                ('pageURL', models.CharField(max_length=400, null=True)),
                ('clientID', models.ForeignKey(db_column='clientID', on_delete=django.db.models.deletion.CASCADE, to='ClientManagementService.client')),
            ],
            options={
                'db_table': 'ClientSitePage',
            },
        ),
        migrations.CreateModel(
            name='CustomerFlow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('flowPercent', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('flowVisitors', models.IntegerField(null=True)),
                ('flowRanking', models.IntegerField(null=True)),
                ('clientID', models.ForeignKey(db_column='clientID', on_delete=django.db.models.deletion.CASCADE, to='ClientManagementService.client')),
                ('keyDataID', models.ForeignKey(db_column='keyDataID', on_delete=django.db.models.deletion.CASCADE, to='KeyDataService.keydata')),
                ('reportID', models.ForeignKey(db_column='reportID', on_delete=django.db.models.deletion.CASCADE, to='KeydabraManagerController.report')),
            ],
            options={
                'db_table': 'CustomerFlow',
            },
        ),
        migrations.CreateModel(
            name='HeatMap',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heatMapRank', models.IntegerField(null=True)),
                ('collateralID', models.IntegerField(null=True)),
                ('clientSitePageID', models.ForeignKey(db_column='clientSitePageID', on_delete=django.db.models.deletion.CASCADE, to='VisualInsightService.clientsitepage')),
                ('reportID', models.ForeignKey(db_column='reportID', on_delete=django.db.models.deletion.CASCADE, to='KeydabraManagerController.report')),
            ],
            options={
                'db_table': 'HeatMap',
            },
        ),
        migrations.CreateModel(
            name='FlowPageOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pageOrder', models.IntegerField(null=True)),
                ('clientSitePageID', models.ForeignKey(db_column='clientSitePageID', on_delete=django.db.models.deletion.CASCADE, to='VisualInsightService.clientsitepage')),
                ('customerFlowID', models.ForeignKey(db_column='customerFlowID', on_delete=django.db.models.deletion.CASCADE, to='VisualInsightService.customerflow')),
                ('reportID', models.ForeignKey(db_column='reportID', default=1, on_delete=django.db.models.deletion.CASCADE, to='KeydabraManagerController.report')),
            ],
            options={
                'db_table': 'FlowPageOrder',
            },
        ),
    ]
