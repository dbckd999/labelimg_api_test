# Generated by Django 4.2.3 on 2023-07-28 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labelimg', '0004_delete_testmodel_alter_mymodel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]