# Generated by Django 3.2.5 on 2021-12-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagementService', '0002_auto_20211229_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
