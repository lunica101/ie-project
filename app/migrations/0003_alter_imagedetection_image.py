# Generated by Django 4.2.2 on 2023-09-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_imagedetection_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedetection',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]
