# Generated by Django 4.2.3 on 2023-08-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(upload_to='pics/carousel_image/'),
        ),
    ]
