# Generated by Django 4.1.1 on 2022-10-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(1, 'Animals'), (2, 'Cars'), (3, 'Nature'), (4, 'Comment')], null=True),
        ),
    ]
