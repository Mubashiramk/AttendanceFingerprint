# Generated by Django 3.0.2 on 2020-02-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0003_auto_20200211_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendancetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(help_text='Student ID', max_length=20, unique=True, verbose_name='Student ID')),
                ('cname', models.CharField(help_text='class', max_length=20, unique=True, verbose_name='class')),
                ('date', models.CharField(help_text='date', max_length=20, unique=True, verbose_name='date')),
                ('hour', models.CharField(help_text='hour', max_length=20, unique=True, verbose_name='hour')),
                ('status', models.CharField(help_text='status', max_length=20, unique=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'attendance',
                'verbose_name_plural': 'attendance details',
            },
        ),
        migrations.AlterField(
            model_name='studenttable',
            name='status',
            field=models.CharField(default='A', help_text='Status: P/A', max_length=10, null=True, verbose_name='Status'),
        ),
    ]
