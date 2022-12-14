# Generated by Django 3.2.5 on 2021-10-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SummaryDXIInsightService', '0006_alter_statements_statementtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='summaryinsights',
            name='BehavioralDXI',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='summaryinsights',
            name='KPIDXI',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='summaryinsights',
            name='TransactionalDXI',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='summaryinsights',
            name='VisualDXI',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='statements',
            name='statementType',
            field=models.CharField(choices=[('INFER', 'Inference'), ('OBSER', 'Observation'), ('PRED', 'Prediction'), ('RECOM', 'Recommendation'), ('INSIGHT', 'Insight'), ('PRESC', 'Prescription'), ('HEATMAP', 'Heatmap'), ('SENTIMENT', 'SentimentalAnalysis')], max_length=10),
        ),
        migrations.AlterField(
            model_name='summaryinsights',
            name='netDollarValue',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]
