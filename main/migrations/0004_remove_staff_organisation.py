# Generated by Django 3.1.5 on 2021-12-23 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_staff_organisation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='organisation',
        ),
    ]