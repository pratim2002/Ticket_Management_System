# Generated by Django 2.0.7 on 2018-08-14 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticket_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='attached_file',
            field=models.FileField(blank=True, null=True, upload_to='ticket_file/'),
        ),
    ]
