# Generated by Django 2.2.4 on 2019-12-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewattendance', '0003_classroom_dept_student_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(help_text='Branch name', max_length=30, unique=True, verbose_name='Branch Name')),
            ],
        ),
        migrations.DeleteModel(
            name='Dept',
        ),
    ]
