# Generated by Django 3.1.5 on 2021-12-23 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='organisation',
        ),
    ]