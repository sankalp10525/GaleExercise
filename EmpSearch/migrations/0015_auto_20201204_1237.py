# Generated by Django 3.1.3 on 2020-12-04 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpSearch', '0014_auto_20201204_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Employee',
        ),
        migrations.AddField(
            model_name='employee',
            name='Project',
            field=models.ManyToManyField(to='EmpSearch.Project'),
        ),
    ]