# Generated by Django 4.1.3 on 2022-12-15 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0005_auto_20220302_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='salary',
        ),
    ]
