# Generated by Django 3.1.1 on 2021-03-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_maker', '0021_auto_20210312_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='current',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='type',
            field=models.CharField(choices=[('Job', 'Job'), ('Internship', 'Internship')], default='Beginner', max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillset',
            name='experience',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='qualification',
            field=models.CharField(choices=[('PhD', 'PhD'), ('Masters', 'Masters'), ('Bachelors', 'Bachelors'), ('High School', 'High School')], max_length=25),
        ),
    ]