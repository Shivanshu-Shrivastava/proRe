# Generated by Django 3.1.7 on 2021-02-27 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_maker', '0005_posmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='acaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic', models.CharField(max_length=250)),
            ],
        ),
    ]
