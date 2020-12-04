# Generated by Django 3.1.3 on 2020-12-03 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmpSearch', '0008_auto_20201204_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='EmpSearch.project'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AssignProject',
        ),
    ]