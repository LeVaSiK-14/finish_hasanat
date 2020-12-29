# Generated by Django 3.1.2 on 2020-12-29 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0013_projects_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='tags',
        ),
        migrations.AddField(
            model_name='images_news',
            name='sub_title',
            field=models.CharField(default='', max_length=2048),
        ),
        migrations.AddField(
            model_name='images_news',
            name='title',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='tags',
            name='img',
            field=models.ImageField(blank=True, upload_to='Tags_images/'),
        ),
        migrations.AddField(
            model_name='tags',
            name='sub_title_tags',
            field=models.CharField(default='', max_length=2048),
        ),
        migrations.AlterField(
            model_name='images_news',
            name='image',
            field=models.ImageField(blank=True, upload_to='News_multiple_images/'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='tag_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.CreateModel(
            name='SubTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_tags_name', models.CharField(default='', max_length=255)),
                ('sub_title', models.CharField(default='', max_length=2048)),
                ('img', models.ImageField(blank=True, upload_to='Sub_tags_images/')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.tags')),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='sub_tag',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='sites.subtags'),
        ),
    ]