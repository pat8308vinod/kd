# Generated by Django 3.2.5 on 2021-12-29 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ClientManagementService', '0001_initial'),
        ('AuthenticationService', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('isActive', models.BooleanField(null=True)),
                ('createdDate', models.DateTimeField(null=True)),
                ('updatedDate', models.DateTimeField(auto_now_add=True)),
                ('designation', models.CharField(max_length=20)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=25)),
                ('editFlag', models.BooleanField()),
                ('clientID', models.ForeignKey(db_column='clientID', on_delete=django.db.models.deletion.CASCADE, to='ClientManagementService.client')),
                ('roleID', models.ForeignKey(db_column='roleID', default=3, on_delete=django.db.models.deletion.CASCADE, to='AuthenticationService.role')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]