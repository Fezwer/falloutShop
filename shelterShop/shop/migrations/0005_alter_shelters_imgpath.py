# Generated by Django 5.0.4 on 2024-06-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_shelters_imgpath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelters',
            name='imgPath',
            field=models.ImageField(upload_to='imgShelters', verbose_name='Изображение'),
        ),
    ]