# Generated by Django 3.1.2 on 2020-12-29 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0016_auto_20201229_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=128)),
                ('title_2', models.CharField(default='', max_length=128)),
                ('sub_title', models.CharField(default='', max_length=2048)),
                ('sub_title_2', models.CharField(default='', max_length=2048)),
                ('collapse_title_1', models.CharField(default='', max_length=128)),
                ('collapse_sub_title_1', models.CharField(default='', max_length=1280)),
                ('collapse_title_2', models.CharField(default='', max_length=128)),
                ('collapse_sub_title_2', models.CharField(default='', max_length=1280)),
                ('collapse_title_3', models.CharField(default='', max_length=128)),
                ('collapse_sub_title_3', models.CharField(default='', max_length=1280)),
                ('collapse_title_4', models.CharField(default='', max_length=128)),
                ('collapse_sub_title_4', models.CharField(default='', max_length=1280)),
                ('img', models.ImageField(upload_to='Products_images/')),
                ('img_2', models.ImageField(blank=True, default='', upload_to='Products_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Images_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='Products_multiple_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.products')),
            ],
        ),
    ]
