# Generated by Django 3.2.25 on 2024-03-11 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0012_course_internship_major_project_mini_project_session_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instructor.course')),
                ('internship_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instructor.internship')),
                ('major_project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instructor.major_project')),
                ('mini_project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instructor.mini_project')),
                ('session_year_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instructor.session_year')),
            ],
        ),
    ]
