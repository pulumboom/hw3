# Generated by Django 4.1.3 on 2022-11-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiencedescriptionpoints',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='projectdescriptionpoints',
            name='project',
        ),
        migrations.AddField(
            model_name='projects',
            name='project_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='project_description_draft',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='ExperienceDescriptionPoints',
        ),
        migrations.DeleteModel(
            name='ProjectDescriptionPoints',
        ),
    ]
