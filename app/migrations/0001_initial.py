# Generated by Django 4.2.2 on 2023-09-15 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageDetection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='detection')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageSummery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_type', models.IntegerField(choices=[(0, 'HmeeKhor (หมี่ขอ)'), (1, 'Heart (หัวใจ)'), (2, 'HmorNam (หม้อน้ำ)'), (3, 'HmeeRuad (หมี่รวด)'), (4, 'BrokenThread (เส้นยืนขาด)'), (5, 'HitchSilk (ขี้ไหม)'), (6, 'SlackThread (เส้นยืนหย่อน)')])),
                ('accuracy', models.FloatField(blank=True, help_text='cof in yolo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image_detect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.imagedetection')),
            ],
        ),
    ]
