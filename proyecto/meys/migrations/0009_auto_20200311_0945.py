# Generated by Django 2.2.4 on 2020-03-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meys', '0008_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.FileField(upload_to='archivos/'),
        ),
    ]
