# Generated by Django 4.1.1 on 2022-10-05 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_delete_student_remove_studentprofile_dob_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
        migrations.DeleteModel(
            name='TeacherProfile',
        ),
    ]
