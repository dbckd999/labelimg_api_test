# Generated by Django 4.2.3 on 2023-07-28 06:46

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labelimg', '0005_alter_mymodel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
        ),
    ]