# Generated by Django 3.2.5 on 2022-03-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TransactionService', '0008_alter_cnnsimilarproduct_similarityscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnnrecommender',
            name='reportName',
            field=models.CharField(default='ACDF', max_length=50),
        ),
        migrations.AddField(
            model_name='cnnsimilarproduct',
            name='reportName',
            field=models.CharField(default='ACDF', max_length=50),
        ),
        migrations.AddField(
            model_name='topproduct',
            name='reportName',
            field=models.CharField(default='ACDF', max_length=50),
        ),
        migrations.AddField(
            model_name='transactionsummary',
            name='reportName',
            field=models.CharField(default='ACDF', max_length=50),
        ),
    ]