# Generated by Django 2.0.7 on 2018-08-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_auto_20180815_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('PROBLEM', 'Problem'), ('FEATURE REQUIRED', 'Feature Required'), ('SUGGESTION', 'Suggestion'), ('OFFICIAL', 'Official')], max_length=40),
        ),
    ]