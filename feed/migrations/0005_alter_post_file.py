# Generated by Django 4.0.6 on 2022-09-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_post_file_post_title_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to='f`media/files/ {super().ID}`'),
        ),
    ]
