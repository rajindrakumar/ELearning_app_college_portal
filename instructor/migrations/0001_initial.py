# Generated by Django 5.0.1 on 2024-02-20 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Instructor_d",
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
                ("full_name", models.CharField(max_length=122)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=12)),
                ("password", models.CharField(max_length=124)),
            ],
        ),
    ]
