# Generated by Django 3.1.3 on 2021-02-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_maker', '0015_auto_20210224_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mobile_no',
            field=models.IntegerField(max_length=12),
        ),
    ]
