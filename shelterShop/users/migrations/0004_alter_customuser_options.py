# Generated by Django 5.0.4 on 2024-06-12 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Баланс', 'verbose_name_plural': 'Балансы'},
        ),
    ]
