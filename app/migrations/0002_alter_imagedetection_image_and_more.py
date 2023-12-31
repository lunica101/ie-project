# Generated by Django 4.2.2 on 2023-09-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedetection',
            name='image',
            field=models.ImageField(max_length=255, upload_to='detection'),
        ),
        migrations.AlterField(
            model_name='imagesummery',
            name='image_type',
            field=models.IntegerField(choices=[(0, 'HmeeKhor (หมี่ขอ)'), (1, 'Heart (หัวใจ)'), (2, 'HmorNam (หม้อน้ำ)'), (3, 'HmeeRuad (หมี่รวด)'), (4, 'BrokenThread (เส้นยืนขาด)'), (5, 'HitchSilk (ขี้ไหม)'), (6, 'SlackThread (เส้นยืนหย่อน)')]),
        ),
    ]
