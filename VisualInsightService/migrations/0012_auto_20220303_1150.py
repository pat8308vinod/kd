# Generated by Django 3.2.5 on 2022-03-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisualInsightService', '0011_alter_topfeature_significance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorsegmentation',
            name='compositeDXI',
            field=models.DecimalField(decimal_places=15, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='visitorsegmentation',
            name='significance',
            field=models.DecimalField(decimal_places=7, max_digits=50, null=True),
        ),
    ]
