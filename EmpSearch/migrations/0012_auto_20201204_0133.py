# Generated by Django 3.1.3 on 2020-12-03 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmpSearch', '0011_auto_20201204_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpSearch.employee'),
        ),
    ]
