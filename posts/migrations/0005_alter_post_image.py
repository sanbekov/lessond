# Generated by Django 4.1.1 on 2022-09-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
    ]
