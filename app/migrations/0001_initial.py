# Generated by Django 4.1.2 on 2023-01-06 12:06

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ani_class', models.CharField(max_length=10)),
                ('ani_type', models.CharField(max_length=10)),
                ('likes_cat', models.CharField(max_length=3)),
                ('likes_kids', models.CharField(max_length=3)),
                ('size', models.CharField(max_length=10)),
                ('activity_level', models.CharField(max_length=10)),
                ('bio', models.CharField(max_length=225)),
                ('ani_image', models.ImageField(default='compound/default.jpg', upload_to=app.models.upload_to, verbose_name='Image')),
            ],
        ),
    ]
