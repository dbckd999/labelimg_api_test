# Generated by Django 4.1 on 2023-07-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labelimg", "0002_alter_mymodel_photo"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("txval", models.CharField(max_length=20)),
            ],
        ),
    ]
