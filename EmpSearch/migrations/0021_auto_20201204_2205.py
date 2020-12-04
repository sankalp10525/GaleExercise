# Generated by Django 3.1.3 on 2020-12-04 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmpSearch', '0020_auto_20201204_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Project',
        ),
        migrations.AddField(
            model_name='project',
            name='employee',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='display', to='EmpSearch.employee'),
            preserve_default=False,
        ),
    ]