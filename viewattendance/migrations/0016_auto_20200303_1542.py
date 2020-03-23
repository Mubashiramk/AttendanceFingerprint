# Generated by Django 3.0.3 on 2020-03-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewattendance', '0015_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(null=True, verbose_name='Roll Number'),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('student_id', 'course_id', 'hour', 'date')},
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('student_id', 'class_id', 'roll_no')},
        ),
    ]
