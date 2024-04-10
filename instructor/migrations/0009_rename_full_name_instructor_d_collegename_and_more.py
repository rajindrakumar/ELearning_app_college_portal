# Generated by Django 5.0.1 on 2024-03-02 14:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructor", "0008_alter_instructor_d_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="instructor_d",
            old_name="full_name",
            new_name="CollegeName",
        ),
        migrations.RemoveField(
            model_name="instructor_d",
            name="about",
        ),
        migrations.RemoveField(
            model_name="instructor_d",
            name="certificate",
        ),
        migrations.RemoveField(
            model_name="instructor_d",
            name="education",
        ),
        migrations.RemoveField(
            model_name="instructor_d",
            name="experience",
        ),
        migrations.RemoveField(
            model_name="instructor_d",
            name="location",
        ),
        migrations.RemoveField(
            model_name="instructor_d",
            name="profile_pic",
        ),
        migrations.RemoveField(
            model_name="instructor_d",
            name="skills",
        ),
        migrations.AddField(
            model_name="instructor_d",
            name="CollegeCode",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="instructor_d",
            name="adminAdministrator",
            field=models.CharField(default=django.utils.timezone.now, max_length=122),
            preserve_default=False,
        ),
    ]
