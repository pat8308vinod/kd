# Generated by Django 3.2.5 on 2021-09-02 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AuthenticationService', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('companyName', models.CharField(max_length=100)),
                ('companyAddress', models.CharField(max_length=200)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('isActive', models.BooleanField(null=True)),
                ('isEnabled', models.BooleanField(null=True)),
                ('isEcommerce', models.BooleanField(null=True)),
            ],
            options={
                'db_table': 'Client',
            },
        ),
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('isActive', models.BooleanField(null=True)),
                ('createdDate', models.DateTimeField(null=True)),
                ('updatedDate', models.DateTimeField(auto_now_add=True)),
                ('designation', models.CharField(max_length=20)),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AuthenticationService.usercredentials')),
                ('clientID', models.ForeignKey(db_column='clientID', on_delete=django.db.models.deletion.CASCADE, to='ClientManagementService.client')),
                ('roleID', models.ForeignKey(db_column='roleID', default=3, on_delete=django.db.models.deletion.CASCADE, to='AuthenticationService.role')),
            ],
            options={
                'db_table': 'ClientUser',
            },
        ),
    ]
