# Generated by Django 4.1.2 on 2023-01-06 12:53

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_animal_likes_cat_alter_animal_likes_kids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='ani_image',
            field=models.ImageField(default='asset_img/default.jpg', upload_to=app.models.upload_to, verbose_name='Image'),
        ),
    ]
