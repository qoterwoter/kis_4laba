# Generated by Django 3.1.5 on 2021-12-23 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_staff_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='organisation',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.organisation'),
            preserve_default=False,
        ),
    ]
