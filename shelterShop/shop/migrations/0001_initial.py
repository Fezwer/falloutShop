# Generated by Django 5.0.4 on 2024-05-23 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Согласование...', max_length=50, verbose_name='Название')),
                ('imgPath', models.CharField(max_length=250, verbose_name='Изображение')),
                ('description', models.TextField(default='Описание пока отсутствует, обратитесь к администратору с этой проблемой.', verbose_name='Описание')),
                ('price', models.PositiveIntegerField(default=999999999, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Убежища',
            },
        ),
    ]
