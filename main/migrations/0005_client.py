# Generated by Django 3.1.5 on 2021-12-23 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_hotels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Имя')),
                ('full_name', models.TextField(verbose_name='ФИО')),
                ('sex', models.CharField(choices=[('м', 'Мужской'), ('ж', 'Женский')], max_length=1, verbose_name='Пол')),
                ('photo', models.TextField(verbose_name='Фотография')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('birthplace', models.TextField(verbose_name='Место рождения')),
                ('passport_series', models.IntegerField(verbose_name='Серия паспорта')),
                ('passport_number', models.IntegerField(verbose_name='Номер паспорта')),
                ('passport_date', models.DateField(verbose_name='Дата выдачи')),
                ('passport_date_end', models.DateField(verbose_name='Дата окончания действия')),
                ('agency', models.TextField(verbose_name='Орган выдавший документ')),
                ('status', models.CharField(choices=[('Привелигированный', 'Привелигированный'), ('Обычный', 'Обычный'), ('VIP', 'VIP')], max_length=25)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
