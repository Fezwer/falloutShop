# Generated by Django 5.0.4 on 2024-06-12 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Баланс', 'verbose_name_plural': 'Балансы'},
        ),
    ]
