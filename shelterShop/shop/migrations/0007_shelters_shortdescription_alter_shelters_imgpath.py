# Generated by Django 5.0.4 on 2024-06-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_shelters_imgpath'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelters',
            name='shortDescription',
            field=models.TextField(default='Описание пока отсутствует, обратитесь к администратору с этой проблемой.', max_length=100, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='shelters',
            name='imgPath',
            field=models.ImageField(upload_to='imgShelters', verbose_name='Изображение'),
        ),
    ]