# Generated by Django 3.1.1 on 2021-03-12 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_maker', '0020_auto_20210312_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='status',
            field=models.CharField(choices=[('Pursuing', 'Pursuing'), ('Completed', 'Completed')], max_length=25),
        ),
    ]
