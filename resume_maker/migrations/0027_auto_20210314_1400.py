# Generated by Django 3.1.1 on 2021-03-14 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_maker', '0026_auto_20210314_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='left_dt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='end_dt',
            field=models.DateField(blank=True, null=True),
        ),
    ]
