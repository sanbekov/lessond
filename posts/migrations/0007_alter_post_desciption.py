# Generated by Django 4.1.1 on 2022-10-11 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desciption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
