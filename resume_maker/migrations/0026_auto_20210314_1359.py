# Generated by Django 3.1.1 on 2021-03-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_maker', '0025_projects_running'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='end_dt',
            field=models.DateField(null=True),
        ),
    ]